import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json
def app():
    query_id ="0564c7df-f6f2-4f14-bf8e-816594ab431c"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)    

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    df = px.bar(df, x = "DATE" , y = "ETHEREUM_UNIQUE_WALLETS" , title = "yay" , orientation = "v" , template = "plotly_white" ,  width = 1000, height = 600, log_y = t_f)