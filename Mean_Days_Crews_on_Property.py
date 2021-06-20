# TODO: find the mean for crews between certain date
#  filter for crew we need and dates dont for get!


import pandas as pd
import time

fileName = "Northern Branch Phase II Debris Removal Ops.xlsx" #insert your file name here
df = pd.read_excel(fileName)

# TODO: variable for crews needed and property status
# our variables
todaysDate = time.strftime("%m-%d-%y")
status = ("Withdrawal", "Ineligible") # will use to take those properties out
# if we only need certain crews change as needed
active_crews = ["CREW#101", "CREW#102", "CREW#203", "CREW#301", "CREW#404", "CREW#501", "CREW#406", "CREW#304", "CREW#701",
                "CREW#702", "CREW#703", "CREW#704", "CREW#705", "CREW#706",
                "CREW#707" "CREW#708", "CREW#801", "CREW#802", "CREW#803", "CREW#805"]
def mean_crew_days_on_propert(df):
    # filter out withdrawals and ineligible properties and dates needed
    df = df.copy()
    start_date = input("Put your start day in this format 2021-05-01: ")
    end_day = input("Put your end day in this format 2021-06-19: ")

    df.loc[:, ['Debris Start', 'Debris Finish']] = df[(df.loc[:, 'Debris Start'] >= start_date) &
                                                      (df.loc[:, 'Debris Finish'] <= end_day)]
    df.loc[:,  "Structural Status"] = df.loc[:, "Structural Status"].isin(status)

    # Duration is the finish day minus start day
    df.loc[:, "Duration"] = df.loc[:, 'Debris Finish'] - df.loc[:, 'Debris Start']

    # convert 'duration' column to a float instead of timedelta64[ns]
    df["Duration"] = df["Duration"].dt.days

    # Filter columns we need
    df = df[['APN', "Structural Status", 'County', 'Debris Crew', 'Debris Crew WO#', 'Debris Start',
             'Debris Finish', 'Duration']]

    # RE for filtering for debris crews. Gets rid of extra text and fixes formatting issues leaving "crew # and number"
    df['Debris Crew WO#'] = df['Debris Crew WO#'].str.extract('(CREW ?# ?\d+)')

    # take out the spaces in 'Debris Crew WO#'
    df['Debris Crew WO#'] = df['Debris Crew WO#'].str.replace(" ", "")

    # use only active crews. Comment this line out to get all crews. Shortcut key for commenting out a line = CTRL + /
    df.loc[:, 'Debris Crew WO#'] = df[df.loc[:, 'Debris Crew WO#'].isin(active_crews)]

    # group by county and dbres crew showing the means days on property for each crew.
    dffilt = df.groupby(['County', 'Debris Crew WO#'])[["Duration"]].mean()

    #saves an excel for emailing
    dffilt.to_excel("Mean days on property " + todaysDate + ".xlsx")
    #prints it to the screen as well
    return df.groupby(['County', 'Debris Crew WO#'])[["Duration"]].mean().round(2)


print(mean_crew_days_on_propert(df))














