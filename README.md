# Readme.md


# Python Files you'll need to use and what they do 
* peerreviews.py - takes the unzipped files in submissions and puts them into to_send with updated filenames, updates master.csv
* send_files - sends files to the students from to_send based on Canvas ID
* send_reviews - once you have reviews from students, iterates through the reviews and grabs any review associated with each student ID, then emails the reviews to each student
* csv_grader - goes through the reviews and produces a grade for each student, output to grades.csv
* prep_gradebook - puts grades and gradebook together -> upload.csv, which you can upload to Canvas
* fixgradebook - located in rosterandgradebook, appends the caesar roster with the canvas roster to give you output.csv. You'll use this in your other files to deal with Canvas IDs and emails

# CSV files and what they do 
* upload.csv - the adjusted gradebook that you'll upload to Canvas -- be sure to change the name from "grade" to whatever the assignment is in Canvas
* roster.csv - roster from Caesar
* reviews.csv - list of reviews from google forms in a CSV, you can get rid of the columns we don't care about
* master.csv - which canvas ID is peer reviewing other Canvas IDs
* grades.csv - made by csv_grader.py, used by prep_gradebook.py
* gradebook.csv - gradebook, downloaded from Canvas

# Instructions
* Download roster from Caesar
* Download gradebook from Canvas
* Download submissions from Canvas as a Zip, unpack to ./submissions
* run fixgradebook.py, adjust to fit roster.csv
* run peerreviews.py
* run send_files.py -- make sure you edit the send_files() function to contain your email info
* WAIT FOR PEER REVIEWS
* Download reviews.csv from google form, edit out extraneous info
* run csv_grader.py -> grades.csv
* run prep_gradebook.py -> upload.csv 
* upload.csv to canvas
* run send_reviews.py -> send all reviews to students via email -- make sure you edit the send_files() function to contain your email info