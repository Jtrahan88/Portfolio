import pandas as pd

fileName = 'North Branch CA Wildfires - Parcel Issues.csv'

treeDf = pd.read_csv(fileName, usecols= ['APN','Tree Survey Date', 'House Number', 'Street Address',
                                           'Are there hazards present on the property?', 'County','Number of Trees',
                                           'Crew Leader', 'Arborist'], index_col='APN')

treeDf.to_excel("Test Csv File.xlsx")
