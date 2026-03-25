#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib
from email.message import EmailMessage
from datetime import date
import os


# In[2]:


def send_csv_email(file_path, subject, receiver, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = os.getenv("EMAIL_SENDER")#"gfernandes2108@gmail.com"
    msg['To'] = os.getenv("EMAIL_RECEIVER") #  receiver #

    # email body
    msg.add_alternative(body, subtype='html')

    # attach csv file
    with open(file_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='text',
            subtype='csv',
            filename=file_path
        )

    #send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(os.getenv("EMAIL_SENDER"),os.getenv("EMAIL_PASS"))
        server.send_message(msg)

    print("Email sent!")


# In[3]:


today = date.today().strftime("%Y-%m-%d")

file_path = f"../data/exports/export_last_month_delivery_loads_{today}.csv"

subject = f"Daily Report - Last Month Delivery Loads ({today})"

receiver = "ghab12@hotmail.com"

body = f"""
<html>
  <body>
    <h2>Daily Report - Last Month Delivery Loads</h2>

    <p>Hello,</p>

    <p>This report contains all loads delivered in the last completed month based on the latest available data.</p>

    <p><b>Report date:</b> {today}</p>

    <p>The file is attached in CSV format.</p>

    <br>

    <p>Best regards,<br>
  </body>
</html>
"""

send_csv_email(file_path, subject, receiver, body  )

