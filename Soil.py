import pandas as pd


fileName = 'TT_Northern Branch_Soil.csv'

Soildf = pd.read_csv(fileName, header=1, usecols= ['APN','Street Number', 'Street Name','County', 'Date Collected',
                                                     'Number of Samples Collected', 'Date Shipped',
                                                     'State\'s Rec on Confirmation Sample','CalRecycle Final Decision']
                       , index_col='APN')

Soildf.to_excel("Test the csv file.xlsx")
