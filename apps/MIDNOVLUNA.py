import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
   


    query_id = "c5dc74dd-a633-455f-afd5-f17d4723bb78"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
 

    

# 43394653-19ab-4b48-a210-8f8315647b47



    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = ["LUNAPRICE","PRICEBLUNA","LUNAPREMIUM","LUNAPREMIUMPCT"],
        # color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "LUNA PRICES",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    # DAYZ	LUNAPRICE	PRICEBLUNA	LUNAPREMIUM	LUNAPREMIUMPCT


    query_id = "1ea09912-27c6-46b1-aa7c-3908f12e27de"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  

    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "DAYYZ",
        y = "SUM(BALANCE)",
        # color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "LUNA Circulating",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    # 59b34585-a70f-49b8-aa50-43076b8ccd0e
    query_id = "59b34585-a70f-49b8-aa50-43076b8ccd0e"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  

    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "DAYYZ",
        y = "SUM(BALANCE)",
        # color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "UST CIRCULATING",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)