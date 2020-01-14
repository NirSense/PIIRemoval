# PIIRemoval
A simple script to hash PII from excel files of a specific format

## Execution
Simply run

`$ python3 hash_students.py`

A dialouge to choose a directory should pop up. Choose the directory that _contains_ the student folders.

## Output
The script will create a folder name `out` and a file named `student_hashes.csv` in the directory containing the student folders. The `out` folder will contain the .xlsx files without any PII. The names of these files are the keys to mapping back any said file to the student who authored it. The `student_hashes.csv` file contains a table of such file names (SHA1 hashed student names/ids/netids) paired with the orginal hashed data of the appropriate file.