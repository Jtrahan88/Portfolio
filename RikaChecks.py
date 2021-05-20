import pandas as pd
import openpyxl


fileNameSS = ""

dfRika = pd.read_excel(fileNameSS, engine="openpyxl")
# df = dfRika.set_index("County")

#TODO: Total Counts
def RikaChecks(dfSS):
    groupbyCheck = df.groupby('County').count()
    whatWeAreCounting = groupbyCheck.loc[:,["Haz Trees","ROE Verified", "Withdrawal", "Not Eligible", 'Hold', "Site Assessment", "ASB Assessment"]]
    # whatWeAreCounting.to_excel("RikaTest.xlsx")