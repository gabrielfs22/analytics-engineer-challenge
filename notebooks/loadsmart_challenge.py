#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv


# In[2]:


def split_lane(lane):
    # split pickup and delivery in two parts using "->"
    pickup, delivery = lane.split("->")

    # split city and state using "," and remove spaces
    pickup_city, pickup_state = pickup.strip().split(",")
    delivery_city, delivery_state = delivery.strip().split(",")

    return {
        "pickup_city": pickup_city.strip(),
        "pickup_state": pickup_state.strip(),
        "delivery_city": delivery_city.strip(),
        "delivery_state": delivery_state.strip()

    }


# In[3]:


# importing csv
raw_loadsmart_database = pd.read_csv("../data/2026_data_challenge_ae_data.csv")


# In[4]:


# remove duplicated column
raw_loadsmart_database = raw_loadsmart_database.drop(columns=['has_mobile_app_tracking.1'])

# remove duplicated rows
raw_loadsmart_database = raw_loadsmart_database.drop_duplicates()

# remove line breaks
raw_loadsmart_database = raw_loadsmart_database.replace('\n', ' ', regex=True)
raw_loadsmart_database = raw_loadsmart_database.replace('\r', ' ', regex=True)

# converting datetimes
raw_loadsmart_database["delivery_date"] = pd.to_datetime(raw_loadsmart_database["delivery_date"])
raw_loadsmart_database["source_date"] = pd.to_datetime(raw_loadsmart_database["source_date"])
raw_loadsmart_database["pickup_date"] = pd.to_datetime(raw_loadsmart_database["pickup_date"])
raw_loadsmart_database["book_date"] = pd.to_datetime(raw_loadsmart_database["book_date"])
raw_loadsmart_database["quote_date"] = pd.to_datetime(raw_loadsmart_database["quote_date"])
raw_loadsmart_database["pickup_appointment_time"] = pd.to_datetime(raw_loadsmart_database["pickup_appointment_time"])
raw_loadsmart_database["delivery_appointment_time"] = pd.to_datetime(raw_loadsmart_database["delivery_appointment_time"])


# apply the split_lane function to each row, turning the dictionary into columns
raw_loadsmart_database[['pickup_city','pickup_state','delivery_city','delivery_state']] = \
raw_loadsmart_database['lane'].apply(split_lane).apply(pd.Series)
raw_loadsmart_database = raw_loadsmart_database.drop(columns=['lane'])


# In[5]:


# exporting csv
raw_loadsmart_database.to_csv("../dbt_project/seeds/loadsmart_database.csv", index=False)

