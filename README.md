# DisasterWork_Python
#This will be the updated Python verision from https://github.com/Jtrahan88/DisasterWork_VBA.git



#                           **in progress**


#TODO: Import openpyxl, pandas, numpy
from openpyxl import load_workbook

#TODO: Open and read the excel files i need start with main file. add adtional files later
#select our excel file "manually"
workbook = load_workbook(filename= "test.xlsx")

# here to print out our worksheet names, if we need to make our sheet variable. Will keep commentedout
#print(workbook.worksheets) 
 #we can now us our sheet variable to pul data from the sheet as we need
 
sheet = workbook["Northern Branch Phase II Debris"]


#TODO: i want to either hvae a widown open and i can ut multiple excell files to be read or
#TODO: an input box where we can type it in each file.

 



#TODO: Copy aolumn A (APNs) to a new workbook

