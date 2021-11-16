import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json
query_id = input("api/query_id")
print("query_id" + query_id)



def app():

    query_id = query_id
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True

    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = week,
        y = "FROMM",
        color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "1. Active Weekly Users",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    