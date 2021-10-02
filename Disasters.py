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

# make columns. Once named we can assign data to that column
# TODO: make a header columns that has total laid out for user





st.markdown("---")

st.title("Total Disasters by Type in the USA")

# Key Performance Indicator's  (KPI's)
st.subheader(f"You are viewing the following states: {State}")

# by declaration
# TODO: assign to a column-right side
declaration_totals = df_selection['declaration_title'].value_counts()
st.bar_chart(declaration_totals)

st.markdown('---')


# by Total incidents
# TODO: assign to a column - left side
incidents_total = df_selection['incident_type'].value_counts()
st.bar_chart(incidents_total)









# TODO: example gcode i made ignoe but use as referance



# import pandas as pd
# import openpyxl
# import streamlit as st
# import plotly.express as px
#
#
#
# # to run streamlit run yourscript.py in command promt
#
# def get_data_from_excel():
#     df = pd.read_excel(io="supermarkt_sales.xlsx", #our data set
#                       engine='openpyxl',
#                       sheet_name='Sales',
#                       skiprows=3,
#                       usecols='B:R',
#                       nrows=1000)
#
#     #title page Upper left side
#     st.set_page_config(page_title='Sales Dashboard',
#                       page_icon=':bar_chart:',
#                       layout='wide')
#
#     # add 'hour' column to dataframe
#     df["hour"] = pd.to_datetime(df['Time'], format="%H:%M:%S").dt.hour
#     return df
# df = get_data_from_excel()
# # st.dataframe(df)
#
# st.sidebar.header('Please Filter Here:')
# City = st.sidebar.multiselect(
#     "Select the City:",
#     options=df['City'].unique(),
#     default=df['City'].unique()
# )
#
# Customer_type = st.sidebar.multiselect(
#     "Select the Customer_type:",
#     options=df['Customer_type'].unique(),
#     default=df['Customer_type'].unique()
# )
#
# Gender = st.sidebar.multiselect(
#     "Select the Gender:",
#     options=df['Gender'].unique(),
#     default=df['Gender'].unique()
# )
#
#
# df_selection = df.query(
#     "City == @City & Customer_type == @Customer_type & Gender == @Gender"
# )
#
# # st.dataframe(df_selection)
#
#
# #----- MAinPAge -----
#
# st.title(':bar_chart: Sales Dashboard')
# st.markdown("##")
#
#
# # Top KPI's
# total_sales = int(df_selection['Total'].sum())
# average_rating = round(df_selection['Rating'].mean(), 1)
# star_rating = ":star:" * int(round(average_rating, 0))
# average_sale_by_transaction = round(df_selection['Total'].mean(), 2)
#
#
# left_column, middle_column, right_column = st.columns(3)
# with left_column:
#     st.subheader('Total Sales:')
#     st.subheader(f"US $ {total_sales:,}")
# with middle_column:
#     st.subheader('Average Rating:')
#     st.subheader(f"{average_rating} {star_rating}")
# with right_column:
#     st.subheader('Average Sales Per Transaction:')
#     st.subheader(f"${average_sale_by_transaction}")
#
# st.markdown("---")
#
#
#
# # sales by product line [Bar Chart]
#
# sales_by_product_line = (
#     df_selection.groupby(by=['Product line']).sum()[['Total']].sort_values(by='Total')
# )
# fig_product_sales = px.bar(
#     sales_by_product_line,
#     x='Total',
#     y=sales_by_product_line.index,
#     orientation='h',
#     title="<b>Sales by Product Line</b>",
#     color_discrete_sequence=['#0083B8'] * len(sales_by_product_line),
#     template="plotly_white",
# )
# # takes out grey back ground and
# fig_product_sales.update_layout(
#     plot_bgcolor='rgba(0,0,0,0)',
#     xaxis=(dict(showgrid=False))
# )
# # st.plotly_chart(fig_product_sales)
#
#
#
#
#
# # 2nd Chart Sale by hour
# sales_by_hour = df_selection.groupby(by=['hour']).sum()[['Total']]
# fig_hourly_sales = px.bar(
#     sales_by_hour,
#     x=sales_by_hour.index,
#     y='Total',
#     title="<b>Sales by hour</b>",
#     color_discrete_sequence=['#0083B8'] * len(sales_by_hour),
#     template="plotly_white",
# )
# fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode='linear'),
#     plot_bgcolor='rgba(0,0,0,0)',
#     yaxis=(dict(showgrid=False)),
# )
#
# left_column, right_column = st.columns(2)
# left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
# right_column.plotly_chart(fig_product_sales, use_container_width=True)
#
#
# # ---Hide Streamlit Style ----
# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header{visibility: hidden;}
# </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)
#
#





