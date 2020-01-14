#!/usr/local/bin/python3


'''
Folder Structure
 - Root Dir
	 - Student 1
	 	- Submission attachment(s)
	 		- Student #1.xlsx
	 	- timestamp.txt
	 - Student 2
	  	- Submission attachment(s)
	 		- Student #2.xlsx
	 	- timestamp.txt
We'll remove authorship meta data from the files.
Hash the filename containing the students names/id
Hash cell D2 where the student name appears
Save a table of student identifiers for the identification of students locally.
'''

from easygui import diropenbox
import os
import glob
import hashlib
import openpyxl



top_level_dir = diropenbox()


student_hashes_map = {}


out_dir = os.path.join(top_level_dir, "out")
if not os.path.exists(out_dir):
	os.mkdir(out_dir)


for student_dir in glob.glob(os.path.join(top_level_dir,"*")):
	if not os.path.isdir(student_dir):
		continue #skip non-folders - the expected structure is to find a folder for each student.

	# The folder name is what we'll use as the student ID, hashing it is done here
	student_name = os.path.basename(student_dir)
	hashed_student_name = hashlib.sha1(student_name.encode()).hexdigest()
	student_hashes_map[hashed_student_name] = student_name

	for submission_folder in glob.glob(os.path.join(student_dir, "*")):
		if not os.path.isdir(submission_folder):
			continue

		for xlsx_file in glob.glob(os.path.join(submission_folder, "*.xlsx")):
			#found submission files, change their name, Author property and D2 cell and copy them to the out folder
			student_file = openpyxl.load_workbook(xlsx_file)
			student_file.active["E2"] = hashed_student_name
			student_file.active["D2"] = ""
			student_file.properties.creator = ""
			student_file.save(os.path.join(out_dir,hashed_student_name+".xlsx"))



#Write the hashes->IDs map to a csv
with open(top_level_dir+"/student_hashes.csv", 'w') as csvfile:
	csvfile.write("ID, Hashed_Value\n")
	for k,v in student_hashes_map.items():
		csvfile.write(f"{k}, {v}\n")



