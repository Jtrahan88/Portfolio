import pandas as pd


fileName = 'TT_Northern Branch_Soil.xlsx'

Soildf = pd.read_excel(fileName, header=1, usecols= ['APN','Street Number', 'Street Name','County', 'Date Collected',
                                                     'Number of Samples Collected', 'Date Shipped',
                                                     'State\'s Rec on Confirmation Sample','CalRecycle Final Decision']
                       , index_col='APN')

print(Soildf.columns)