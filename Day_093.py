# ========================= Question ========================
#
# contextlib.contextmanager lets you write a context manager
# as a generator function. Write setup code before yield,
# teardown code after. The yield is where the with block executes.
#
# Write these context managers using @contextlib.contextmanager:
#
# 1. managed_db_connection(connection_string)
#    - Pretend to open/close a DB connection.
#    - Print "Opening connection".
#    - Yield a fake connection object.
#    - Print "Closing connection" always, even on exception.
#
# 2. temp_directory()
#    - Create a temporary directory.
#    - Yield its path.
#    - Delete it and all contents when done.
#    - Use tempfile and shutil.
#
# 3. atomic_write(filepath)
#    - Open a temp file for writing.
#    - Yield the file handle.
#    - On success, rename to target.
#    - On exception, delete the temp file instead.
#
# ============================================================

# ======================== Solution ==========================
# All imports 
from contextlib import contextmanager
import os
import shutil
import tempfile

# 1. managed_db_connection(connection_string)
@contextmanager
def managed_db_connection(connection_string):
    try:
        print("Opening connection")
        connection = {
            "connection_string": connection_string,
            "status": "opened"
        }
        yield connection
    finally:
        print("Closing connection")

# 2. temp_directory()
@contextmanager
def temp_directory():
    try:
        path = tempfile.mkdtemp()
        yield path
    finally:
        shutil.rmtree(path)

# 3. atomic_write(filepath)
@contextmanager
def atomic_write(file_path):
    temp_file = tempfile.NamedTemporaryFile(
        mode = "w",
        delete=False
    )
    try:
        yield temp_file
        temp_file.close()
        shutil.move(temp_file.name, file_path)
    finally:
        temp_file.close()
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)

# ======================== Example Usage =========================
with managed_db_connection("db://localhost") as conn:
    print(conn)

with temp_directory() as path:
    print(f"Temporary directory created at: {path}")
    # You can create files or directories inside this temp directory

with atomic_write("example.txt") as f:
    f.write("Hello, World!")
