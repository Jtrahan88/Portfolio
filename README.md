# DisasterWork_Python
#This will be the updated Python verision from https://github.com/Jtrahan88/DisasterWork_VBA.git



# Python3
# read Smart Sheets file download - unknown how this will read(practicing for work audits)

#                           **in progress**
#Additonal ideas to make this better after orginal product works:
#TODO: Have a windown open and i can ut multiple excel files to be read or
# or
#TODO: an input box where we can type it in each file.


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









# we can now us our sheet variable to pul data from the sheet as we need

sheet = workbook["Northern Branch Phase II Debris"]




# TODO: Copy aolumn A (APNs) to a new workbook
