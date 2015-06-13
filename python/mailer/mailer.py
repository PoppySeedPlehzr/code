#!/usr/bin/env python
import smtplib
import random
import argparse
from email.mime.text import MIMEText

sig = """\n\n
------------------------------------------------------------
A-Non-ee-moose
"""


sig_joke = """\n\n
---------------------------------------------------------------------------------

"""

#SERVERS = open("smtp_servers.txt", 'r').readlines()
#SERVER = "mail.sandia.gov"
#SERVER = "mailgate.sandia.gov"
SERVER = "mail-relay.3ireland.ie"

def mailer(f, t, s, b):
    smtp = smtplib.SMTP(SERVER)
    text = b+sig
    msg = MIMEText(text)
    msg['Subject'] = s
    msg['From'] = f
    msg['to'] = t
    smtp.sendmail(f, t, msg.as_string())
    smtp.quit()
    print "[+] Message sent."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A anonymous smtp mailer client")
    parser.add_argument("sender", help="Email to send from")
    parser.add_argument("--to", "-t", help="Email to send to")
    parser.add_argument("--subject" "-j", help="Message Subject")
    parser.add_argument("--body", "-b", help="Message body")
    args = parser.parse_args()
    mailer(args.to, args.sender, args.subject, args.body)
