#!/usr/bin/env python
# coding: utf-8

# In[1]:


import paramiko
import os
from datetime import date

def send_csv_sftp(local_path, remote_path):

    # host = os.getenv("SFTP_HOST")
    # port = int(os.getenv("SFTP_PORT", 22))
    # username = os.getenv("SFTP_USER")
    # password = os.getenv("SFTP_PASS")
    host = "localhost"
    port = 2222
    username = "user"
    password = "password"


    transport = paramiko.Transport((host,port))
    transport.connect(username=username,password=password)
    print("Connected successfully!") 

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    print("File saved!")

    sftp.close()
    transport.close()
    print(f"File {local_path} sent to {remote_path} via SFTP.")


# In[2]:


today = date.today().strftime("%Y-%m-%d")

file_path = f"../data/exports/export_last_month_delivery_loads_{today}.csv"
remote_path = f"/upload/export_last_month_delivery_loads_{today}.csv"

send_csv_sftp(file_path, remote_path)

