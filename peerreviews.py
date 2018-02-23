import glob
import os
import csv
from zipfile import ZipFile
import re

SUBDIR = "./submissions/"

# get list of submissions
# edit this line to get files
listFiles = glob.glob(SUBDIR + "*.zip")

# initialize list of students 
listStudents = []

# call a write file
writeFileName = "master.csv"
writeFile = open(writeFileName, 'w+')
writeFile.write("Grader ID, Peer Reviews \n")

# rename to only include student id
for file in listFiles:
	print "file = " + str(file)
	studentID = re.search("_[0-9]{4,6}_", str(file)).group(0)
	# memoize student IDs, because we're good little programmers
	listStudents.append(str(studentID))
	print 'ID: ' + str(studentID)
	os.rename(file, SUBDIR + str(studentID) + ".zip")
	file = SUBDIR + str(studentID) + ".zip"


listFiles = glob.glob(SUBDIR + "*.zip")

for i in range(0, len(listFiles)):
	studentID = listStudents[i]
	peerReviews = []
	reviewFiles = []
	
	# prep zip file
	with ZipFile('./tosend/' + studentID + '.zip', 'w') as myZip: 

		# the case where the list wraps
		if listStudents[i] == listStudents[-1]:
			peerReviews = listStudents[0:3]
			reviewFiles = listFiles[0:3]

		elif listStudents[i] == listStudents[-2]:
			peerReviews = listStudents[0:2] + [listStudents[i + 1]]
			reviewFiles = listFiles[0:2] + [listStudents[i + 1]]

		elif listStudents[i] == listStudents[-3]:
			peerReviews = [listStudents[0]] + listStudents[i + 1: i + 2]
			reviewFiles = [listFiles[0]] + listFiles[i + 1: i + 2]
		# the list doesn't wrap 
		else: 
			peerReviews = listStudents[i+1:i+4]
			reviewFiles = listFiles[i+1:i+4]

		# write review files to zip archive
		for file in reviewFiles: 
			try: 
				myZip.write(file)
			except: 
				print "this person needs a folder: " + str(myZip)

		myZip.close()

	# add pairs to CSV for logging purposes
	writeFile.write(studentID + ", " + str(peerReviews) + "\n")

	


