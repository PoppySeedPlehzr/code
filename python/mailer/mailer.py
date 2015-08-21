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

SERVER = open("smtp_servers.txt", 'r').readlines()[0].strip()

def mailer(f, t, s, b):
    smtp = smtplib.SMTP(SERVER)
    if os.path.exists(b):
        b = open(b, 'r').read()
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
    parser.add_argument("--subject" "-s", help="Message Subject")
    parser.add_argument("--body", "-b", help="File with message body")
    args = parser.parse_args()
    mailer(args.to, args.sender, args.subject, args.body)
