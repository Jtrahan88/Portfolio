#TODO: LEft here due to maek need to add more tasks later

import pandas as pd
import time
todaysDate = time.strftime("%m-%d-%y")

soil_file = 'state & Field Tracker/TT_Northern Branch_Soil.xlsx'
df_soil = pd.read_excel(soil_file, header=1) # Soil Data


# TODO: soil_cols(df) ---> get columns ready for VBA
def soil_cols(df):
    df = df[["APN", "Date Collected"]]
    df = df.set_index("APN")
    df.to_excel("Soil data columns " + todaysDate + ".xlsx")
soil_cols(df_soil)
