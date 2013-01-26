import sys
import smtplib
import time

from email.mime.text import MIMEText

msg = MIMEText("zhu")
msg['Subject'] = "From: Course_Monitor"
msg['From'], msg['To'] = "zhaoyan1117@gmail.com", "6262576432@vtext.com"

# Send the message via gmail SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(msg['From'], "Mb680520") 

def send_message(CCN):
    cm = MIMEText(CCN + " is available now")
    cm['Subject'] = "From: Course_Monitor"
    cm['From'], cm['To'] = "zhaoyan1117@gmail.com", "6262576432@vtext.com"
    s.send_message(msg)

i = 1
while (True):
    s.send_message(msg)
    print ("success * " + str(i))
    i+=1
    time.sleep(10)
