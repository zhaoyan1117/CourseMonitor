import time
import sys
import smtplib
from email.mime.text import MIMEText
from urllib.request import urlopen


def get_info(CCN):
    """Access the course info page, break down all the text, and get info.
       Return a list of all the breaking down text of the info page.
       THIS IS FOR FALL 2012 SCHEDULE.
       CCN -- Course Control Number"""
    course_info = urlopen('http://infobears.berkeley.edu:3400/osc/?_InField1=RESTRIC&_InField2=' + str(CCN) + '&_InField3=12D2')
    course_txt=course_info.read().decode().split()
    return course_txt


def cur_enr_num(course_txt):
    """Return the amount of the current enrolled student of the wanted course.
       course_txt -- list of a breaking down version of the course info page"""
    i = course_txt.index('width=80%>')+1
    info = course_txt[i]
    num = eval(info[info.index('>')+1:info.index('&')])
    return num


def limit_enr_num(course_txt):
    """Return the limit enrolling number of the wanted course.
       course_txt -- list of a breaking down version of the course info page"""
    limit = eval(course_txt[course_txt.index('width=80%>')+8])
    return limit


def txt_test(course_txt):
    """In some case, test if 'full,' exists in the txt, if so, the course is full.
       course_txt -- list of a breaking down version of the course info page"""
    if course_txt[course_txt.index('section')+2] == 'full,':
        return True
    return False


def analyse_info(CCN):
    """Analyse all the course info, and return whether the course is full or not.
       CCN -- Course Control Number"""
    course_txt = get_info(CCN)
    try:
        if txt_test(course_txt):
            return "Sorry, no space"
        return "!!!!!!!!Space available!!!Enroll Now!!!!!!!!"
    except ValueError:
        if cur_enr_num(course_txt) < limit_enr_num(course_txt):
            return "!!!!!!!!Space available!!!Enroll Now!!!!!!!!"
        return "Sorry, no space"
    

def check_course(CCN, p):
    """Automatically check the course in a period of p.
       CCN -- Course Control Number
       p -- period of automatically checking the course's availability"""
    while True:
        result=analyse_info(CCN)
        if result == "!!!!!!!!Space available!!!Enroll Now!!!!!!!!":
            s.send_message(cm)
        print(result)
        time.sleep(p)


if __name__ == "__main__":
    CCN = sys.argv[1]
    p = float(sys.argv[2])
    print("Start monitoring course " + CCN + " every " + str(p) + " seconds.")
    cm = MIMEText(CCN + " is available now")
    cm['Subject'] = "From: Course_Monitor"
    cm['From'], cm['To'] = "zhaoyan1117@gmail.com", "6262576432@vtext.com"

    # Send the message via gmail SMTP server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(cm['From'], "Mb680520") 
    check_course(CCN, p)
