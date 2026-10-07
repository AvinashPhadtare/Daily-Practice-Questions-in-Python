# ========================= Question =========================
# You are given a list of file paths.
#
# The number of files is determined at runtime.
#
# Use contextlib.ExitStack to open all files simultaneously.
#
# Read one line from each file in round-robin order:
# first line from file 1, first line from file 2, first line from file 3,
# then second line from file 1, second line from file 2, second line from file 3,
# and so on.
#
# All files must be closed properly, even if an error occurs.
#
# Write a function process_member_files(filepaths: list) -> list that:
# • Opens all files using contextlib.ExitStack
# • Reads the files in round-robin order
# • Returns all lines in the round-robin order
# • Properly closes all files after processing
#
# Create 3 test files with 5 lines each and demonstrate the function.
#
# Example:
#
# Input:
# member1.txt
# member2.txt
# member3.txt
#
# Output:
# Member 1 - Line 1
# Member 2 - Line 1
# Member 3 - Line 1
# Member 1 - Line 2
# Member 2 - Line 2
# Member 3 - Line 2
# Member 1 - Line 3
# Member 2 - Line 3
# Member 3 - Line 3
# Member 1 - Line 4
# Member 2 - Line 4
# Member 3 - Line 4
# Member 1 - Line 5
# Member 2 - Line 5
# Member 3 - Line 5
# ============================================================


# ========================= Solution =========================
# All imports
from contextlib import ExitStack


# Function to process member files in round-robin order
def process_member_files(file_paths: list) -> list:
    with ExitStack() as stack:
        # Open all files using ExitStack
        files = [stack.enter_context(open(fname, "r")) for fname in file_paths]

        result = []
        while files:
            # remaining_files will hold files that still have lines to read
            remaining_files = []

            for f in files:
                line = f.readline()

                if line:
                    
                    result.append(line.strip())
                    remaining_files.append(f) # Keep the file in the list if it has more lines to read

            files = remaining_files
    
    return result


# ========================= Example Usage =========================
# You have to create 3 test files with 5 lines each before running this code.
# named as 'file1.txt', 'file2.txt', and 'file3.txt' in the same directory as this script.

# File names
filenames = ["file1.txt", "file2.txt", "file3.txt"]


# Process files
result = process_member_files(filenames)


# Display result
for line in result:
    print(line)
