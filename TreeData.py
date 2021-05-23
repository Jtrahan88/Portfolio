import pandas as pd

fileName = 'North Branch CA Wildfires - Parcel Issues.xlsx'

treeDf = pd.read_excel(fileName, usecols= ['APN','Tree Survey Date', 'House Number', 'Street Address',
                                           'Are there hazards present on the property?', 'County','Number of Trees',
                                           'Crew Leader', 'Arborist'], index_col='APN')

print(treeDf.columns)