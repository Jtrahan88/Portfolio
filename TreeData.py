#TODO: LEft here due to maek need to add more tasks later

import pandas as pd
import time

todaysDate = time.strftime("%m-%d-%y")
tree_file = 'North Branch CA Wildfires - Parcel Issues.xlsx'

df_tree = pd.read_excel(tree_file, sheet_name="TREE SURVEYS") # Tree Data

def tree_cols(df):
    df = df[["APN", "Tree Survey Date", "Number of Trees"]]
    df = df.set_index("APN")
    df.to_excel("Tree data Columns " + todaysDate + ".xlsx")
tree_cols(df_tree)
