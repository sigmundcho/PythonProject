import time
import serial
import smtplib

TO = 'sigmundcho@wooridisplay.co.kr'
GMAIL_USER = 'sigmundcho@gmail.com'
GMAIL_PASS = 'josua0724'

SUBJECT = 'Intrusion!!'
TEXT = 'Your PIR sensor detected movement'

ser = serial.Serial('COM13', 9600)


def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print
    header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()


while True:
    message = ser.readline()
    print(message)
    if message[0] == 77: #'M':
        send_email()
    time.sleep(0.5)