# Get each review
# Get each ID 
# Match ID to a person
# Send email to person

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import os
import pandas as pd
import time

REVIEWDIR = "./peer_reviews/"

def main():
    roster = pd.read_csv('roster.csv')
    emails = list(roster.email)
    student_ids = list(roster.id)
    student_ids = map(str, student_ids)
    list_ids = []
    list_reviews = []
    dict_emails = dict()
    for file in os.listdir(REVIEWDIR):
        if str(file[-4:]) == '.csv':
            list_reviews.append(file)

    for review in list_reviews: 
        try:
            reviewF = open(REVIEWDIR + review)
            pdFile = pd.read_csv(reviewF)
            for index, row in pdFile.iterrows():
                listcols = [row["id"], row["1"], row["2"], row["3"],row["4"], row["5"], row["6"], row["7"], row["8"], row["9"], row["10"], row["11"], row["12"], row["comments"]]
                student_id = str(listcols[0])
                content = ""
                for col in listcols:
                    content += str(col) + '\n'
                if student_id not in dict_emails:
                    dict_emails[student_id.strip('_')] = content
                else: 
                    dict_emails[student_id.strip('_')] += content
            reviewF.close()
        except Exception as e:
            print e 

    count = 0
    for key, value in dict_emails.iteritems():
        if key in student_ids:
            try:
                print "Sending mail to: " + str(emails[student_ids.index(key)])
                send_mail(emails[student_ids.index(key)], key, value)
            except: 
                print "Couldn't send mail to " + str(emails[student_ids.index(key)])
                print "Continuing again in 60 seconds."
                time.sleep(60)
                continue

            
            


def send_mail(recipient, id, content):
    msg = MIMEMultipart()
    msg['From'] = "YOUR EMAIL"
    msg['To'] = recipient
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "YOUR SUBJECT"

    text = "Hello, " + recipient[:-23] + "YOUR MESSAGE" + content

    msg.attach(MIMEText(text))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login("YOUR EMAIL", "YOUR PASSWORD")
    s.sendmail("YOUR EMAIL", recipient, msg.as_string())
    s.close()


if __name__ == '__main__':
    main()

