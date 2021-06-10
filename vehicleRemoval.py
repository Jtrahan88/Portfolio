
#TODO:
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
import time
# import openpyxl
import matplotlib.pyplot as plt
import numpy as np
# from tkinter import Tk
# from tkinter.filedialog import askopenfile


#TODO: SS Excel Name: make this so I do not have to manually enter it. This Sheet is constanly changing. Maybe webscraping?
# Smart Sheets Workbook variable
fileNameSS = "Northern Branch Phase II Debris Removal Ops.xlsx"


print("Opening Vehicle check program.....")
dfSS = pd.read_excel(fileNameSS)#,usecols= ['APN','Street #', 'Street Name','Debris Finish', 'Number of Vehicles',
                                          #'Number of Vehicles Removed',  'County']) # index_col='APN' do this later after futher editing APNS
#only way to display all columns and rows for my data set
# pd.set_option('display.max_rows', 3000)
# pd.set_option('display.max_columns', 3000)
# pd.options.display.max_columns= None
# pd.options.display.width= None
#TODO: how to make open and close file more automated*



#TODO: vecCheck  ----------------->Columns for vehicle checks

def vecCheck(dfSS):
    dfSS = dfSS[['APN','Street #', 'Street Name','Debris Finish', 'Number of Vehicles',
                 'Number of Vehicles Removed',  'County']]
    dfSS = dfSS.set_index("APN")
    todaysDate = time.strftime("%m-%d-%y")
    dfSS.to_excel("SmartSheet Vehicle Set up " + todaysDate + ".xlsx")
vecCheck(dfSS)


#TODO: SScardCheck  --------------> Checks card locations in SMart Sheets
def SScardCheck(dfSS):
    dfSS = dfSS[['APN', "Debris Crew", "Division", "County", "Debris Crew Leader/Crew#"]]
    dfSS = dfSS.set_index("APN")
    dfSS.to_excel("Card Check.xlsx")
# SScardCheck(dfSS)

#  # df.reset_index(inplace=True) #This will reset the index back to numbers


# dfSS.to_excel("SmartSheet Vehicle Set up.xlsx")

#TODO: Filter APNs for no dahses But ignore the ODD APNS

# removes all dashes then joins that together with no spaces for full APN & remove extras zeros from APNS

uniqueAPNs = ["018-510-02-00_#19A", "018-530-04-00", "018-530-06-00_#17", "018-530-09-00", "018-530-10-00", "020-080-28-00_#24B"
              "020-080-31-00", "020-320-06-00", "020-330-05-00_#105", "020-330-05-00_#106", "020-330-05-00_#107", "020-330-05-00_#110",
              "020-340-14-00", "020-340-22-00", "020-340-36-00", "020-470-01-00", "021-160-13-00", "021-160-23-00",
              "021-160-24-00", "041-330-049-000_12541", "041-330-055-000_house", "044-190-020-000_1", "056-270-010",
              "021-160-25-00", "020-470-04-00", "062-740-020-000_119", "009-490-050-000", "062-760-012-000",
              "062-290-043-000_062-290-045-000" "021-200-20-00", "021-200-21-00", "021-200-23-00", "020-120-23-00",
              "020-100-27-00_#66"]
# 020-100-27-00_#63B
# 020-100-27-00
# 020-070-54-00
# 020-460-11-00
# 020-120-10-00
# 020-120-19-00
# 020-120-21-00
# 020-120-22-00
# 020-070-22-00
# 020-070-46-00_#48
# 021-200-17-00
# 020-320-02-00_#45
# 018-490-01-00
# 020-320-02-00_#39G
# 020-320-02-00_#39H
# 020-320-02-00_#41
# 020-320-02-00_#42
# 020-320-02-00_#43
# 020-320-02-00_#43A
# 020-320-02-00_#44A
# 022-090-16-00
# 018-530-06-00_#23
# 020-470-09-00
# 020-320-02-00_#101F
# 020-320-02-00_#102
# 020-320-07-00
# 020-320-11-00
# 018-510-02-00_#18
# 018-510-02-00_#19
# 022-290-09-00
# 022-010-53-00
# 022-010-56-00
# 022-010-57-00
# 020-490-10-00
# 020-500-02-00
# 020-320-02-00_#46
# 020-540-07-00
# 021-160-20-00
# 021-200-18-00
# 021-200-19-00
# 020-400-04-00
# 020-380-02-00
# 020-510-12-00
# 022-010-40-00
# 022-090-33-00
# 020-330-05-00_#59
# 020-330-06-00
# 020-070-46-00_#52
# 022-080-09-00
# 022-080-18-00
# 022-010-47-00
# 020-320-02-00_#47B
# 020-080-28-00_#31
# 020-080-28-00_#32
# 020-080-28-00_#33
# 020-080-28-00_#34
# 020-080-28-00_#36
# 020-080-28-00_#37
# 018-530-06-00_#97H
# 022-040-16-00
# 020-510-36-00
# 021-210-02-00
# 020-100-32-00_#112B
# 022-040-15-00
# 022-080-33-00
# 022-080-40-00
# 022-090-15-00
# 020-320-02-00_#47A
# 022-090-31-00
# 022-090-32-00
# 020-070-55-00_1
# 020-070-55-00_2
# 020-070-56-00
# 020-510-16-00
# 020-510-17-00
# 020-390-04-00
# 020-390-05-00
# 020-340-04-00
# 020-340-29-00
# 020-390-06-00
# 020-400-01-00
# 020-100-32-00_#112E
# 020-100-32-00_#112H
# 020-100-32-00_#112J
# 020-100-32-00_#112O
# 020-100-32-00_#112P
# 020-080-28-00_#38A
# 020-320-02-00_#44B
# 020-320-02-00_#44C
# 020-320-02-00_#44E
# 020-110-03-00
# 020-100-20-00
# 021-040-01-00
# 019-190-01-00
# 019-190-03-00
# 020-330-05-00_#108
# 020-330-05-00_#109
# 020-330-05-00_#109E
# 020-330-05-00_#111
# 020-330-05-00_#111C
# 020-510-40-00
# 020-520-17-00
# 021-160-18-00
# 021-160-19-00
# 018-530-06-00_#23A
# 020-320-02-00
# 020-320-02-00_#101
# 020-080-25-00_#98B
# 020-070-58-00
# 020-070-46-00_#51
# 018-520-15-00_#94B
# 021-160-22-00
# 022-290-08-00
# 021-190-12-00
# 021-190-13-00
# 021-200-12-00
# 020-080-25-00_#98A
# 020-510-32-00
# 020-120-03-00
# 020-320-04-00
# 020-070-46-00_#53
# 020-070-46-00_#54
# 020-070-46-00_#55
# 020-070-46-00_#56
# 020-070-46-00_#57
# 022-290-13-00
# 022-290-17-00
# 022-290-25-00
# 020-510-24-00
# 020-340-01-00
# 022-110-15-00
# 022-290-05-00
# 022-290-07-00
# 020-300-25-00
# 020-080-28-00_#26A
# 020-080-28-00_#26C
# 020-080-28-00_#27
# 020-080-28-00_#28
# 020-080-28-00_#30
# 018-330-27-00
# 020-320-12-00
# 020-330-02-00
# 021-160-10-00
# 021-160-11-00
# 020-070-46-00_#58A_#58B
# 021-190-09-00
# 021-190-11-00
# 020-040-18-00
# 020-070-01-00
# 020-070-03-00
# 020-070-51-00
# 018-510-03-00
# 018-520-11-00
# 020-100-74-00
# 020-380-14-00
# 018-530-06-00_#20
# 020-080-28-00_#38B
# 020-400-03-00
# 020-080-21-00
# 018-330-26-00
# 020-120-25-00
# 020-100-89-00
# 020-100-97-00
# 020-320-02-00_#39E
# 020-500-07-00
# 020-500-08-00
# 020-070-49-00
# 020-080-28-00_#39F
# 020-400-06-00
# 020-460-08-00
# 020-460-09-00
# 020-510-27-00
# 020-510-28-00
# 020-100-49-00
# 018-340-02-00
# 018-340-05-00
# 018-340-07-00
# 022-010-45-00
# 020-510-11-00
# 021-200-15-00
# 020-100-08-00
# 020-100-14-00
# 020-080-30-00
# 020-080-32-00
# 021-200-14-00
# 020-320-02-00_#39
# 018-520-21-00
# 018-520-24-00
# 018-520-29-00
# 018-330-25-00
# 022-290-10-00
# 022-290-11-00
# 022-290-12-00
# 020-100-27-00_#59B
# 022-010-17-00
# 020-490-06-00
# 020-300-26-00
# 022-340-12-00
# 018-330-28-00
# 018-510-02-00_#96A
# 020-340-30-00
# 020-340-33-00
# 020-100-32-00_#112C
# 020-100-32-00_#112D
# 021-160-21-00
# 018-530-06-00_#24A
# 018-510-02-00_#19B
# 020-470-10-00
# 116-230-47-11
# 116-300-39-11
# 115-110-49-11
# 115-190-17-11
# 044-190-020-000_12049
# 041-330-049-000_12573
# 041-330-055-000_barn
# 009-380-070-000_b
# 009-380-070-000_c
# 009-380-070-000_d
# 009-380-070-000_a
# 009-380-070-000_f
# 009-380-070-000_g
# 009-380-070-000_h
# 009-380-070-000_e
# 009-380-070-000_j
# 071-370-014-000_128
# 071-370-014-000_130
# 071-060-009-000_123
# 071-060-009-000_125
# 071-060-009-000_35
# 062-320-033-000_20
# 062-320-033-000_44
# 062-740-020-000_123
# ]
# TODO: APNsetup ------> filter amodified APNs while skiping the ones in the unique APN list. (Does not work)
def APNsetup(dfSS):
    if ~dfSS["APN"].isin(uniqueAPNs).any():
        dfSS["APN"] = dfSS["APN"].str.replace("-", "").str[:9] #TODO: Works but we need to skip over the Special APNs. Mayb use thing in a DICT?dfSS
    dfSS.to_excel("Test APN func.xlsx")
# APNsetup(dfSS)
# make a dict for trinity and other counties that have special APNs so skip next step and leave as is.

# remove extra zeros from APNS













#TODO: Graph out sheet->get graph to only count numbers, and number >0 ONLY!
def getTotalCounts(dfSS): # this function is for getting counts by any way you need.
    county = dfSS.groupby(['County']).count()  # this will put "COUNTY"on Y-Axis and counts all the values from other columns
    counts = county.loc[:,"Number of Vehicles Removed"]  # left side :  all rows , right side: is the column we want to look at. This is how we chose what we want to ount up
    # counts.to_excel("test3.xlsx") # if we use county we get counts for entier data set columns by county, if we use counts.to_excel() we only get vec removed column.

    # Make a graph based on above.
    counts.plot(kind='bar', x='county', y='counts') # this makes our bar chart from the data.

    #Add number to bar charts
    for i in range(len(county)): # for loop for each element in the lenth of counties, display the height of each row center and at the top of the repectiv bar chart.
        plt.text(i, counts[i], counts[i], ha='center', va='bottom') #i for each index. [i] for the height of counts(the bar/number og vehicles removed)
        # the 2nd count[i] is for numbers but we can put text there

# Graph Add ons
    plt.title('Total Vehicle Removal Counts By County') #title the bar chart
    plt.xlabel("Counties")  # labels the X-Axis on our graph
    plt.ylabel('Vehicles Removed')  # labels the Y-Axis on our graph
    plt.legend()  # add a legend for our graph
    # plt.xticks([1,2,3]) # change to x tick values and how much they go or down by
    # plt.yticks([1,2,3]) # change to y tick values and how much they go or down by
    print(dfSS[["County", "Number of Vehicles Removed"]].groupby("County").count())
    plt.show()  # show or print out the graph to view


# getTotalCounts(dfSS) # test function










