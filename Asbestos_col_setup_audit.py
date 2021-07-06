#TODO: Left here due to maek need to add more tasks later

import pandas as pd
import time

todaysDate = time.strftime("%m-%d-%y")
asb_file = 'state & Field Tracker/TT_North Branch_Asbestos.xlsx'
df_asb = pd.read_excel(asb_file, header=1) # asb data


# TODO: asb_cols(df) ---> get columns ready for VBA
def asb_cols(df):
    df = df.copy()
    df = df.loc[:, ["APN", "Date Collected", "Tt Received Date", "Final Results", "Point Count Needed?", "Point Count Results",
             "Chimney", "NESHAP Walls", "CHIM TIP (DATE)", "Chimney Finding",  "Asbestos Abatement Completed Date",
            "Chimney Abatement Completed Date", "No. of Samples"]]
    df = df.set_index("APN")
    df.to_excel("ASB data columns " + todaysDate + ".xlsx")
asb_cols(df_asb)
