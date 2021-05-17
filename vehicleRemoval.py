
#TODO:
# Filter for columns needed
# FROM SS: ---> SIDE BY SIDE COMPARISON with RTR
#  Graph: GET TOTAL VEHICLE COUNTS AND VEHICLES REMOVED COUNTS FOR EACH COUNTY-make my function a double bar graph
#  Show any mismatch(highlight them, make them pop out in a table with reason, etc)
#  make GUI once everything else is complete.
#  labelThisVarDifferent = askopenfile(title='Select File')  # shows dialog box and return the path
#  Tk.withdraw()


# TODO: Documentation locations:
# pandas:  https://pandas.pydata.org/pandas-docs/stable/
# matplotlib: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
# openpyxl:
# numpy:
#  Smart Sheets vehicle aspects that will be used. only this function will have this. APN = index inplace is False
# 'APN'(made index not needed), 'Street #', 'Street Name', 'Number of Vehicles', 'Number of Vehicles Removed', 'Debris Finish', 'County'

import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfile


#TODO: SS Excel Name: make this so I do not have to manually enter it. This Sheet is constanly changing. Maybe webscraping?
# Smart Sheets Workbook variable
fileNameSS = "Northern Branch Phase II Debris Removal Ops (1).xlsx"


print("Opening Vehicle check program.....")
dfSS = pd.read_excel(fileNameSS, engine="openpyxl") # opens Smartsheets excell refered to as dfSS #TODO: index_col='APN' make this happen-doesn't work
df= dfSS.set_index('APN') # puts APN as INDEX we can add , inplace=True to make it permanent
pd.options.display.width= None #only way to display all columns and rows for my data set 2500cols x 119rows
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)
pd.options.display.max_columns= None
#TODO: how to make open and close file more automated*
#  # df.reset_index(inplace=True) #This will reset the index back to numbers


# TODO: Filter function columns we will use for comparing excel sheets
def vehicleCols(df):
    df = df[['Street #', 'Street Name', 'Number of Vehicles', 'Number of Vehicles Removed', 'Debris Finish', 'County']]
    return df
# dfSS.to_excel("Test.xlsx") #saves to a new excel file
# dfSS.to_excel("Test.xlsx", index= "APN") #saves to a new excel file with no index column. #TODO: find how to make index the APN



# print(findAPN.loc['044-010-064-000'])

# TODO: Function for total vehicle counts after checks. Graph for display*. ******************We need to do comparisions with/before this part******************.
def getTotalVehicleCount(dfSS): # this is for after everything was checked and QC'ed
    county = dfSS.groupby(['County']).count()  # this will put county on Y-Axis and count all the values belonging to each count on the column we want
    counts = county.loc[:,"Number of Vehicles"]  # left side :  all rows , right side: is the column we want to look at.

    counts.plot(kind='bar', x='county', y='counts') # this makes our bar chart from the data.
    for i in range(len(county)): # for loop for each element in the lenth of counties, display the height of each row center and at the top of the repectiv bar chart.
        plt.text(i, counts[i], counts[i], ha='center', va='bottom') #i for each index. [i] for the height of counts(the bar/number og vehicles removed)
        # the 2nd count[i] is for numbers but we can put text there

    plt.title('Total Vehicle Removal Counts By County') #title the bar chart
    plt.xlabel("Counties")  # labels the X-Axis on our graph
    plt.ylabel('Vehicles Removed')  # labels the Y-Axis on our graph
    plt.legend()  # add a legend for our graph
    # plt.xticks([1,2,3]) # change to x tick values and how much they go or down by
    # plt.yticks([1,2,3]) # change to y tick values and how much they go or down by

    plt.show()  # show or print out the graph to view
    print(dfSS[["County", "Number of Vehicles"]].groupby("County").count())  # gets total vehicle counts by county on screen for copy/check(optional)


# print(getTotalVehicleCount(dfSS)) # test function

















