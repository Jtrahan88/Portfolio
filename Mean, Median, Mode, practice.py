#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# import matplotlib as plt
# import numpy as np


# In[2]:


fileName = "Vehicle Check/Northern Branch Phase II Debris Removal Ops.xlsx"
df = pd.read_excel(fileName)


# # Variables to use

# In[3]:


status = ("Withdrawal", "Ineligible") # TODO: make apart of our search 
active_crews = ["101", "102", "203", "301", "404", "501", "406", "304", "701", "702", "703", "704", "705", "706",
                "707" "708", "801", "802", "803", "805"]


# In[ ]:


df.columns.tolist()


# # Get average from start and finish dates of crews
# # Steps:
# ## -Finish days minus start day
# ## -Change data types from timedate to float
# ## -Make data frame only show the columns we need
# ## -Group by county and get the sum, count, and mean of times debris was done on propeties

# In[8]:


df["duration"] = df['Debris Finish'] - df['Debris Start']

df["duration"] = df["duration"].dt.days # convert 'duration' column to a float instead of timedelta64[ns] 

# removal all other columsn from data frame except the following:
df = df[['APN', 'County', 'Debris Crew', 'Debris Crew WO#', 'Debris Start', 'Debris Finish', 'duration']] 
df['Debris Crew WO#'] = df['Debris Crew WO#'].str.extract('(CREW ?# ?\d+)') ### LEARN THIS YESTERDAY!!!!!!

dffilt = df.groupby(['APN', 'County', 'Debris Crew WO#'] ).duration.agg(['sum', 'count', 'mean'])
dffilt.to_excel("Date Averages formatting issue.xlsx") # put it in an excel doc


# # See all columns on screen. *Takes more memory (RAM)

# In[ ]:


pd.set_option('display.max_columns', 120)
pd.set_option('display.max_rows', 2500)


# # Need to filter on the  'Debris Crew WO#' for all chars after crew is read. 
# ## Eaiser way is to grab last 11 chars but not accurate

# In[ ]:


df['Debris Crew WO#'] = df['Debris Crew WO#'].str.extract('(CREW ?# ?\d+)')
df.groupby(['APN', 'Debris Crew WO#'])["duration"].mean()


# In[ ]:





# # See if we can replace all values in Debris Crew WO# with just the actie crews

# In[ ]:


df.loc[:, ['Place Holder']] = df.loc[:, 'Debris Crew WO#'].str[28:] # not very effective due to formatting
df.loc[:, ['Place Holder']]


# In[ ]:


df.loc[:, ['Place Holder']] = df.loc[:, 'Debris Crew WO#'].str[26:]
df.loc[:, ['Place Holder']] = df.loc[:, ['Place Holder']].split().join(" ")


# # Method #1 referring to a list: How to grab just CREW # and number from text
# ## You can use str.extract() with the capture group being a joined list with join('|'). The | symbol is for OR and allows you to search multiple values simultaneously for each row. Capture groups require parentheses around them which is why I add parentheses as strings before and after.

# In[ ]:


df['Debris Crew WO#'] = df['Debris Crew WO#'].str.extract(('(' + '|'.join(active_crews) + ')'))
df['Debris Crew WO#']


# # Method #2 
# ## Extracting based off a regex pattern and ignoring the list. A ? after a space means that the space is optional. Instead of a space you can also do \s or \s+ for multiple spaces. \d+ means consecutive numbers. If there are commas in the numbers, the regex is slightly different:

# In[ ]:


df['Debris Crew WO#'] = df['Debris Crew WO#'].str.extract('(CREW ?# ?\d+)')
df['Debris Crew WO#']


# In[ ]:




