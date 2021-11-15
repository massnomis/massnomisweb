import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
   



    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ef0b2fd1-e03c-4e64-8db3-8c236c59ff9d/data/latest')

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
 

    




    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DHOUR",
        y = "COUNT(POOL_NAME)",
        color = "POOL_NAME",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

#     df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ef0b2fd1-e03c-4e64-8db3-8c236c59ff9d/data/latest')
#     df = px.bar(
#         df, #this is the dataframe you are trying to plot
#         x = "DHOUR",
#         y = ["AMOUNT_STAKED","AMOUNT_UNSTAKEDN"],
#         #color = columns,
#         orientation = "v",
#         template = "plotly_white",
#         width = 1000,
#         height = 600,
#         log_y = t_f
#     )
#     st.plotly_chart(df)    
# # DHOUR	COUNT(POOL_NAME)	POOL_NAME