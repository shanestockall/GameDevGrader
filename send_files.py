import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import os
import pandas
import time


def main():
	roster = pandas.read_csv('roster.csv')
	emails = list(roster.email)
	student_ids = list(roster.id)
	list_ids = []
	for file in os.listdir('./to_send/'):
		list_ids.append(file[1:-5])

	student_ids = map(str, student_ids)

	print list_ids
	print student_ids

	for student_id in list_ids: 
		if student_id in student_ids: 
			for student in student_ids: 
				if str(student) == student_id:
					index = student_ids.index(student)
					email = emails[index]
					try:
						print 'sending files to ' + str(email)
						send_mail(email, student_ids[index])
					except: 
						time.sleep(300)
						list_ids.append(student_ids[index])
						continue





def send_mail(recipient, id):
    msg = MIMEMultipart()
    msg['From'] = "YOUR EMAIL"
    msg['To'] = recipient
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "YOUR SUBJECT"

    # recipient[:-23] gets rid of 20XX@u.northwestern.edu, leaving only the person's name. 
    text = "Hello, " + recipient[:-23] + "YOUR MESSAGE"

    msg.attach(MIMEText(text))

    f = open("./to_send/_" + id + "_.zip", "rb")
    part = MIMEApplication(
    	f.read(),
    	Name="./to_send/_" + id + "_.zip")

    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename=%s' % str(id) + ".zip"
    msg.attach(part)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login("YOUR EMAIL", "YOUR PASSWORD")
    s.sendmail("YOUR EMAIL", recipient, msg.as_string())
    s.close()


if __name__ == '__main__':
	main()
