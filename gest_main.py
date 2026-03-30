#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Simple_Store_Manager ver. 0.1 alpha

from version import Version
import datetime
import warehouse
import navigator

current_time=datetime.datetime.now()
shortener=current_time
shorter_date=datetime.datetime.strftime(shortener, "%d-%m-%Y %H:%M:%S")

print(f"Welcome to --Simple Store Manager-- software version {Version.__version__}")
print(f"Current Date and Time: {shorter_date}")

data=warehouse.Maker()
datacheck=data.isfilealive()
warehouse_maker=data.filemaker()

print(f"Please write 'help' in the command box to learn about all of the software features")
print("-------------------------------")

menu=navigator.Menu()

