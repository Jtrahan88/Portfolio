import pandas as pd
import time

todaysDate = time.strftime("%m-%d-%y") # to add dates to our file

#File name variable
smartsheets_file = 'state & Field Tracker/Northern Branch Phase II Debris Removal Ops (1).xlsx'
tree_file = 'state & Field Tracker/North Branch CA Wildfires - Parcel Issues.xlsx' # need to open specific sheet will not work as of now
sa_file = "state & Field Tracker/TT_North Branch_Site Assessment.xlsx"
asb_file = 'state & Field Tracker/TT_North Branch_Asbestos.xlsx'
soil_file = 'state & Field Tracker/TT_Northern Branch_Soil.xlsx'

# opens our files
df_ss = pd.read_excel(smartsheets_file) #Smart Sheets
df_tree = pd.read_excel(tree_file, sheet_name="TREE SURVEYS") # Tree Data
df_sa = pd.read_excel(sa_file, header=1) # SA data
df_asb = pd.read_excel(asb_file, header=1) # asb data
df_soil = pd.read_excel(soil_file, header=1) # Soil Data


# TODO: smart_sheets_cols(df) --> get colums ready fro VBA
#  remove timefrom date time columns* Tricky due t0 they are objects and not Datetime maybe?
def smart_sheets_cols(df):
    df = df[["APN", "County", "Structural Status", "Site Assessment", "Chimney", "NESHAP Walls",
             "Chimney Tipped", "Number of Vehicles", "Haz Trees Assessment", "# of Trees",
             "ASB Assessment", "ASB Results Received", "ASB Results", "ASB Abatement",
             "Number of Vehicles Removed", "Soil Sample"]]
    status = ("Ineligible", "Withdrawal") # double check the case sensitive aspects of these words
    df = df[(~df["Structural Status"].isin(status))] # take out withdrawn and ineligible properties
    # df["ASB Abatement"] = pd.to_datetime(df["ASB Abatement"])
    # df["ASB Abatement"] = df["ASB Abatement"].dt.date
    df = df.set_index("APN")
    df.to_excel("Smart Sheets Audit Column set up " + todaysDate + ".xlsx")
smart_sheets_cols(df_ss)

# TODO: tree_cols(df) ---> get columns ready for VBA
#  will have to select a different sheet to edit. Not shet one!!
def tree_cols(df):
    df = df[["APN", "Tree Survey Date", "Number of Trees"]]
    df = df.set_index("APN")
    df.to_excel("Tree data Columns" + todaysDate + ".xlsx")
tree_cols(df_tree)

# TODO: sa_cols(df) ---> get columns ready for VBA
#  Sa has the columns on line two. Go back fins out how to remedy this again
def sa_cols(df):
    df = df[["APN", "Date Completed", "Automobiles"]]
    df = df.set_index("APN")
    df.to_excel("SA data Columns " + todaysDate + ".xlsx")
sa_cols(df_sa)

# TODO: asb_cols(df) ---> get columns ready for VBA
#  Sa has the columns on line two. Go back fins out how to remedy this again
def asb_cols(df):
    df = df[["APN", "Date Collected", "Tt Received Date", "Final Results", "Point Count Needed?", "Point Count Results",
             "Chimney", "NESHAP Walls", "CHIM TIP (DATE)", "Chimney Finding",  "Asbestos Abatement Completed Date",
            "Chimney Abatement Completed Date", "No. of Samples"]]
    df = df.set_index("APN")
    df.to_excel("ASB data columns " + todaysDate + ".xlsx")
asb_cols(df_asb)

# TODO: soil_cols(df) ---> get columns ready for VBA
#  Sa has the columns on line two. Go back fins out how to remedy this again
def soil_cols(df):
    df = df[["APN", "Date Collected"]]
    df = df.set_index("APN")
    df.to_excel("Soil data columns" + todaysDate + ".xlsx")
soil_cols(df_soil)
