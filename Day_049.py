# ============================================================
# Question
# ============================================================
#
# Build a SafeJSONStore class — a simple file-based key-value
# store that is safe for concurrent access.
#
# Implement the following methods:
#
# 1. get(key) -> any
#    - Read and return the value for the given key.
#    - Return None if the key does not exist.
#
# 2. set(key, value)
#    - Write or update a key-value pair.
#
# 3. delete(key)
#    - Remove the given key from the store.
#
# 4. all_keys() -> list
#    - Return a list containing all keys.
#
# Requirements:
#
# - Use atomic writes:
#     Write data to a temporary file first,
#     then use os.replace() to replace the original JSON file.
#
# - Use the filelock library to prevent concurrent writes.
#
# - If filelock is unavailable, implement a manual lock-file
#   mechanism:
#     Create a .lock file before writing and delete it after.
#
# - If the lock file is more than 5 seconds old, consider it
#   a stale lock and remove it.
#
# - The backing store must be a single JSON file.
#
# ============================================================


import json
import os
import time
import tempfile
from contextlib import contextmanager


class SafeJSONStore:

    def __init__(self, filepath):
        # Store the path of the JSON file.
        self.filepath = filepath

        # Lock file will have the same name with .lock added.
        self.lockpath = filepath + ".lock"

    # --------------------------------------------------------
    # Acquire a lock
    # --------------------------------------------------------
    @contextmanager
    def _lock(self):

        try:
            # Try to use the filelock library.
            from filelock import FileLock

            # Create a FileLock object.
            lock = FileLock(self.lockpath, timeout=5)

            # Acquire the lock.
            with lock:
                yield

        except ImportError:
            # filelock is not installed.
            # Use our own manual lock-file mechanism.

            while True:

                try:
                    # O_CREAT  -> create the file
                    # O_EXCL   -> fail if file already exists
                    #
                    # This makes lock creation atomic.
                    fd = os.open(
                        self.lockpath,
                        os.O_CREAT | os.O_EXCL | os.O_WRONLY
                    )

                    # Write information about the process/time
                    # into the lock file.
                    with os.fdopen(fd, "w") as lock_file:
                        lock_file.write(str(time.time()))

                    # Lock successfully acquired.
                    break

                except FileExistsError:

                    # Lock already exists.
                    # Check whether it is stale.

                    try:
                        lock_age = time.time() - os.path.getmtime(
                            self.lockpath
                        )

                        # If lock is older than 5 seconds,
                        # consider it stale.
                        if lock_age > 5:
                            os.remove(self.lockpath)
                            continue

                    except FileNotFoundError:
                        # Another process removed the lock.
                        continue

                    # Wait a little before trying again.
                    time.sleep(0.1)

            try:
                # Code inside this block owns the lock.
                yield

            finally:
                # Always remove the lock after the operation.
                try:
                    os.remove(self.lockpath)
                except FileNotFoundError:
                    pass

    # --------------------------------------------------------
    # Read JSON data
    # --------------------------------------------------------
    def _read(self):
        # If the JSON file doesn't exist,
        # start with an empty dictionary.
        if not os.path.exists(self.filepath):
            return {}

        # Open the JSON file for reading.
        with open(self.filepath, "r", encoding="utf-8") as file:
            return json.load(file)

    # --------------------------------------------------------
    # Atomic write
    # --------------------------------------------------------
    def _atomic_write(self, data):

        # Get directory of the JSON file.
        directory = os.path.dirname(
            os.path.abspath(self.filepath)
        )

        # Create a temporary file in the SAME directory.
        fd, temp_path = tempfile.mkstemp(
            dir=directory,
            prefix=".tmp_",
            suffix=".json"
        )

        try:

            # Convert the file descriptor into a normal file object.
            with os.fdopen(fd, "w", encoding="utf-8") as temp_file:

                # Write formatted JSON.
                json.dump(
                    data,
                    temp_file,
                    indent=4
                )

                # Make sure Python sends buffered data
                # to the operating system.
                temp_file.flush()

                # Force the data to be written to disk.
                os.fsync(temp_file.fileno())

            # Atomically replace the original file
            # with the completed temporary file.
            os.replace(
                temp_path,
                self.filepath
            )

        except Exception:

            # If something goes wrong,
            # remove the temporary file.
            if os.path.exists(temp_path):
                os.remove(temp_path)

            raise

    # --------------------------------------------------------
    # get(key)
    # --------------------------------------------------------
    def get(self, key):

        # Acquire lock while reading.
        with self._lock():

            # Read the JSON data.
            data = self._read()

            # Return the value.
            # dict.get() automatically returns None
            # if the key doesn't exist.
            return data.get(key)

    # --------------------------------------------------------
    # set(key, value)
    # --------------------------------------------------------
    def set(self, key, value):

        # Only one process can modify the file at a time.
        with self._lock():

            # Read existing data.
            data = self._read()

            # Add or update the key.
            data[key] = value

            # Write the complete dictionary atomically.
            self._atomic_write(data)

    # --------------------------------------------------------
    # delete(key)
    # --------------------------------------------------------
    def delete(self, key):

        # Acquire the lock before modifying the file.
        with self._lock():

            # Read existing data.
            data = self._read()

            # Remove the key if it exists.
            data.pop(key, None)

            # Write the updated data atomically.
            self._atomic_write(data)

    # --------------------------------------------------------
    # all_keys()
    # --------------------------------------------------------
    def all_keys(self):

        # Acquire the lock while reading.
        with self._lock():

            # Read the JSON data.
            data = self._read()

            # Return all keys as a list.
            return list(data.keys())


# ============================================================
# Example Usage
# ============================================================

store = SafeJSONStore("gym_data.json")

# Add data
store.set("name", "Avinash")
store.set("age", 22)
store.set("plan", "Premium")

# Read data
print(store.get("name"))
print(store.get("age"))

# Missing key
print(store.get("city"))

# Get all keys
print(store.all_keys())

# Delete a key
store.delete("age")

# Check keys again
print(store.all_keys())
