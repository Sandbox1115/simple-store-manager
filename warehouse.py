#!/usr/bin/env python
# coding: utf-8

# In[5]:


from os.path import isfile
import csv

class Maker():

    """
    The "maker" class contains functions for creating and opening the "warehouse.csv" and "stats_file.csv" file, 
    which is used to read and write the data entered by the user. 
    Both 'warehouse.csv' and "stats_file.csv" are opened/created when the software starts.
    """
    
    def __init__(self):
        pass

    def filemaker(self):

        """
        filemaker() generates the stats_file.csv and warehouse.csv files to make sure they are "True" when the program
        starts each time. The files are immediately closed to make sure they are available for other functions/modules
        operations.

        """
        storage=open("warehouse.csv", "a+")
        storage.close()
        stats_file=open("stats_file.csv", "a+")
        stats_file.close()
        return

    def writeheader(self):

        """
        After verifying and creating the 'warehouse.csv' file, the 'writeheader' function writes the CSV file's header with the columns 
        that will be used to store the data entered by the customer. If the header already exists, the function does nothing.

        NOTE: This function is not currently implemented in the final version of the software, but I have decided to keep it for possible 
        future use.
        """
        
        fields=["Product ID", "Product name", "Quantity", "Company price", "Retail price"]
        with open("warehouse.csv", "r") as csvfile:
            try:
                reader=csv.reader(csvfile)
                row1=next(reader)
            except:
                with open("warehouse.csv", "a+", encoding="UTF-8", newline="") as csvfile:
                    writer=csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
            return

    def isfilealive(self):

        """
        Function of the Maker class that checks for the existence of the "warehouse.csv" and "stats_file.csv" 
        in the software directory. If the file is present, it notifies the user that it has been detected. 
        If the file is absent, it informs the user that the file will be created.
        """
        
        wfile=isfile("warehouse.csv")
        sfile=isfile("stats_file.csv")

        if wfile==True:
            print("Warehouse file available already, your stock data has been loaded successfully.")
        else:
            print("warehouse.csv file created successfully.")

        if sfile==True:
            print("stats_csv file available already, your stats data has been loaded successfully.")
        else:
            print("Statistcs stats.csv file created successfully.")
        return


# In[ ]:




