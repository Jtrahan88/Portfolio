
# TODO:
# FROM SS: ---> SIDE BY SIDE COMPARISON
#  GET TOTAL VEHICLE COUNTS AND VEHICLES REMOVED COUNTS FOR EACH COUNTY
#  WE NEED TO ALSO SHOW STREET #, ADDRESS, DEBRIS REMOVAL DATE
#  Show any mismatch(highlight them, make them pop out in a table with reason, etc)


# TODO: Documentation locations:
# pandas:  https://pandas.pydata.org/pandas-docs/stable/
# matplotlib: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
# openpyxl:
# numpy:
#  RTR Data vehicle aspects that will be used. only this function will have this.
# "Zone Name", "End Time", "Is Void", "Ticket Notes", "Service Code", "Unit Count", "Disposal Monitor Name", "Addr No", "Addr St", "Ticket Number"

import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfile

# TODO: make this so I do not have to manually enter it. This Sheet is constanly changing. Maybe webscraping?

#TODO: make GUI once everything else is complete.
#     labelThisVarDifferent = askopenfile(title='Select File')  # shows dialog box and return the path
#     # Tk.withdraw()


# RTR Workbook variable
fileNameRTR = "cCalRecycle_NorthBranch_DataManagerTicketExport.csv"

print("Opening Vehicle check program.....")
dfRTR = pd.read_csv(fileNameRTR,usecols=["Zone Name", "End Time", "Is Void", "Ticket Notes",
                                           "Service Code", "Unit Count", "Disposal Monitor Name", "Addr No",
               "Addr St", "Ticket Number"], index_col="Zone Name")
pd.options.display.width= None #only way to display all columns and rows for my data set 2500cols x 119rows
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)
pd.options.display.max_columns = None
#TODO: how to make open and close file more automated*


# TODO:
#  filter the data for service codes "4" (Go Ahead) and "C04" (Go Back) and for voild ==False only
  # .isin was the key for this. MAKE A YOUTUBE ON THIS 5+hrs to figure this out.

# dfRTR.to_csv('Test.csv')
# dfRTR.replace("CO4 ","CO4")
# dfRTR.replace("4 ", "4")

def getRTRVecCols(dfRTR):
    dfRTR['Service Code'] = dfRTR['Service Code'].str.replace(r'\W', "") #TODO: Learn more about Regex!!!
    filt = dfRTR[(dfRTR['Is Void'] != True) & dfRTR["Service Code"].isin(["CO4", "4"])]
    filt.to_excel('VecTest.xlsx')

#  Figure out the weird APNs(In Zone Name), by hard coding, what they need to look like.
#           Examples: 0203200600 should = 020-320-06-00 | 0203300500_#105 should = 020-330-05-00_#105
#  The rest of the APNs by adding dashes and -000 for example 123456789 need to look like 123-456-789-000


# dfRTR.to_excel("TestRTR.xlsx", index=False) # RTR save to an excel file if needed





# TODO: Function for otal vehicle counts afeter checks. Graph for display*. ******************We need to do comparisions with/before this part******************.

#TODO: Make a function that; get all the columns we need and compare to other excel sheet(s)
# Rearrange column orders for RTR Data:















