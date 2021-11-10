


import plotly
import streamlit as st
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("SOME NICE THORCHAIN LP DATA")

    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f9e6e5b4-b92d-4554-8072-7812ae5a5345/data/latest')



    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    

    st.dataframe(df)

    st.markdown("""
    """)
    



    df2 = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/efd43e88-da50-4496-8d8b-6fa1f02a09c5/data/latest')



    df2 = px.bar(
        df2, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "ADD_LIQUIDITY_COUNT_BY_DAY",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df2)
    df2 = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/efd43e88-da50-4496-8d8b-6fa1f02a09c5/data/latest')



    df2 = px.bar(
        df2, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "USD_ADDED_FOR_DAY",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df2)

    df3 = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f03912cf-aa7e-46f9-8d68-955fbef4b29a/data/latest')



    df3 = px.bar(
        df3, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "REMOVE_LIQUIDITY_COUNT_BY_DAY",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df3)

    df3 = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f03912cf-aa7e-46f9-8d68-955fbef4b29a/data/latest')



    df3 = px.bar(
        df3, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "USD_REMOVED_FOR_DAY",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df3)
# https://api.flipsidecrypto.com/api/v2/queries/f9e6e5b4-b92d-4554-8072-7812ae5a5345/data/latest
# PCT
# ADD_LIQUIDITY_COUNT	REMOVE_LIQUIDITY_COUNT	REMOVE_TO_ADD_PERCENT
# https://api.flipsidecrypto.com/api/v2/queries/efd43e88-da50-4496-8d8b-6fa1f02a09c5/data/latest
# IN
# DAY	ADD_LIQUIDITY_COUNT_BY_DAY	USD_ADDED_FOR_DAY
# https://api.flipsidecrypto.com/api/v2/queries/f03912cf-aa7e-46f9-8d68-955fbef4b29a/data/latest
# out
# DAY	REMOVE_LIQUIDITY_COUNT_BY_DAY	USD_REMOVED_FOR_DAY