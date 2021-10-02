import pandas as pd
import openpyxl
import streamlit as st
import plotly.express as px


# to run
# # streamlit run yourscript.py
# #in command prompt
df = pd.read_csv('us_disaster_declarations.csv', usecols=['state', 'fy_declared', 'incident_type', "declaration_title"])

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

st.title("Total Disasters by Type in the USA")

# Key Performance Indicator's  (KPI's)
st.subheader(f"You are viewing the following states: {State}")

# by declaration
declaration_totals = df_selection['declaration_title'].value_counts()
st.bar_chart(declaration_totals)


# by Total incidents
incidents_total = df_selection['incident_type'].value_counts()
st.bar_chart(incidents_total)




