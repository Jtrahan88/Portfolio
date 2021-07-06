import pandas as pd
import numpy as np


sa_file = "state & Field Tracker/TT_North Branch_Site Assessment.xlsx"
df_sa = pd.read_excel(sa_file, header=1) # SA data

# TODO: sa_cols(df) ---> get columns ready for VBA
def sa_cols(df):
    df = df.copy()
    df = df.loc[:, ["APN", "Date Completed", "Automobiles"]]
    df = df.set_index("APN")
    df.to_excel("SA data Columns " + todaysDate + ".xlsx")
sa_cols(df_sa)



#TODO: Make this a GUI
def chooseYourAPN():
    userInput = input("What APN To search For: ")
    if userInput == '':
        print("\n~Finished~")
    elif userInput not in df.index:
        print("No APN Found\n")
        chooseYourAPN()
    else:
        print(df.loc[userInput])
        chooseYourAPN()


# chooseYourAPN()



