import pandas as pd
import numpy as np


SAdf = 'TT_North Branch_Site Assessment.xlsx'

# df = pd.read_excel(SAdf, engine="openpyxl")
df = pd.read_excel(SAdf, header=1, usecols=['APN','ST No.', 'Unit No.', 'ST Address', 'COUNTY','Date Completed',
                                            'Automobiles','Chimney','Notes'],index_col='APN')
# df = pd.read_excel(SAdf, header=1, index_col="APN")
# pd.options.display.width = None
# pd.options.display.max_columns= None
# pd.set_option('display.max_rows', 2200)
# pd.set_option('display.max_columns', 2200)

#TODO: Make this a GUI
def chooseYourAPN():
    userInput = input("What APN To search For: ")
    if userInput == '':
        print("Finished")
    elif userInput not in df.index:
        print("No APN Found")
        chooseYourAPN()
    else:
        print(df.loc[userInput])
        chooseYourAPN()


chooseYourAPN()




# df.to_excel("test.xlsx")
# df.to_excel("test.xlsx")