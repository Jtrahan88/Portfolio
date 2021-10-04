import pandas as pd
import openpyxl
import streamlit as st
import plotly.express as px


# to run
# # streamlit run yourscript.py
# #in command prompt
df = pd.read_csv('us_disaster_declarations.csv', usecols=['state', 'fy_declared', 'incident_type',
                                                          "declaration_title", "designated_area",
                                                          "fema_declaration_string"])

st.set_page_config(page_title='Disaters by State',
                      page_icon=':earth_americas:',
                      layout='wide')


# #title page Upper left side
# st.set_page_config(page_title="USA Disasters by Year and Disaster.",
#                    page_icon=':bar_chart:',
#                    layout='wide')

# TODO: above dose not work yet come back

# st.dataframe(df) # just here to test when we started

# ---------------------SideBar-------------------
st.sidebar.header('Filters Below:') # side bar header

Year = st.sidebar.multiselect( #to set up sidebar(s)
    "Select the Year:",
    options=df['fy_declared'].unique(),
    default=[2020]
)

State = st.sidebar.multiselect(
    "Select the State:",
    options=df['state'].unique(),
    default=['LA']
)

Incident_Type = st.sidebar.multiselect(
    "Select the Incident Type:",
    options=df['incident_type'].unique(),
    default=['Hurricane']
)


# main page use query, like, SQL that will link our data to our charts
df_selection = df.query(
    "fy_declared == @Year & state == @State & incident_type == @Incident_Type"
)

st.dataframe(df_selection)



#---------------------MAIN PAGE-------------------

# make columns. Once named we can assign data to that column
# TODO: make a header columns that has total laid out for user





st.markdown("---")

# st.title("Total Disasters by Type in the USA")

# Key Performance Indicator's  (KPI's)
st.subheader(f"You are viewing the following states: {State}")

# our columns
left_column, right_column = st.columns(2)

# KPI: by declaration
declaration_totals = df_selection['declaration_title'].value_counts()
# TODO: assign to a column-right side
with right_column:
    st.bar_chart(declaration_totals)

# TODO: does not work need to play around with data
# "designated_area" forcountys and parishes
# df["designated_area"] = df["designated_area"].str.split("(")[0][0]
# designated_area_totals = df["designated_area"].value_counts
# with middle_column:
#     st.bar_chart(designated_area_totals)

# KPI by Total incidents
incidents_total = df_selection['incident_type'].value_counts()
# TODO: assign to a column - left side
with left_column:
    st.bar_chart(incidents_total)




st.markdown('---')









