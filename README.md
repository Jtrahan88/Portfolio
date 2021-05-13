# ! Python3
# read Smart Sheets file download - unknown how this will read(practice lesson)

#                           **in progress**
#TODO: Additonal ideas to make this better after orginal product works correctly:

#TODO: step 2 Have a windown open and i can ut multiple excel files to be read or
# or
#TODO: an input box where we can type it in each file.

#TODO: step 9 Eventually I would like like to look at the ID and plot out the difference with the why in a new worksheet

# Step 1

# import libraries we need
# TODO: see if we can use and import pandas, numpy, malplot
import openpyxl

# Step 2

# have python open the excel file in question. We need to have it downloaded
#TODO: Get this from the dowloads folder. Lastest version downloaded.
print("Opening workbook...")  #read( or open) the Spread Sheet Data in python
wb = openpyxl.load_workbook('PUT EXCEL FILE NAME HERE')# BE SURE TO FILL IN FILE NAME NEEDS TO HAVE .XLSX AT THE END OF FILE NAME

# Step 3(optional)

# now we need to select the work sheet(s) we may need.
# here to print out our worksheet names, so we do not have to open work book
# print(workbook.worksheets) # take off # so see what worksheets are in excel. This is not needed for program to work

# Step 4

# TODO: select worksheet we will start to work with
sheet = wb['']#PUT THE SHEET NAME HERE.Now we can call on that sheet to work with.

# Step 5

# TODO: move this work sheet data to a new PRE MADE AUDIT work sheet.

# Step 6

#TODO: I want to select the column A APNs, only, and copy and past them to a worksheet called Audit
#this worksheet will be pre-made before step 5 happens


# Step 7

#TODO: I want to select certain column headings.
# Easy start for practice we will just go for Site Assessment(SA) comparisons at this time
# Comparision will involving multiple other worksheets to compare

#TODO: This columns formating will be used in the SA tracker only for these heading. Our main sheet will have these
# plus many others

# SA headings we need: APN, Date Completed, Automobiles
# in Smart Sheets the above headings read as: APN, Date Completed, Automobiles
# ***This is very important because other tracker labeled aspect different than the main Smart Sheet racker*****



# Step 8*

#TODO: This step could be included with step 5
#we have to get all the data from multiple worksheets  compare to the audit work sheet



# Step 9

#TODO: set up a vlookup or hlookup to use the ID(APNs in our aduit sheet to grab the iform  SS and SA sheets
# and put both outputs in the audit sheet.
# 1st just putting them side by side is fine. Maybe highlgh any differences.
# Evenutally i would like like to look at the ID and plot out the difference with the why in a new worksheet




