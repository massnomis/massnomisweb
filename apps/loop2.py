import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("YEET")

    query_id = "c96f0ab3-0f21-40bf-883a-90b566ed4320"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )


    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    

    st.dataframe(df)

    st.markdown("""
    """)
    

    


    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "FIRST_TX",
        y = "IN_TX",
        color = "SUM_RANK",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    query_id = "c96f0ab3-0f21-40bf-883a-90b566ed4320"
    df4 = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )
    df4 = px.scatter(
        df4, #this is the dataframe you are trying to plot
        x = "FIRST_TX",
        y = "OUT_TX",
        color = "SUM_RANK",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df4) 
    query_id = "c96f0ab3-0f21-40bf-883a-90b566ed4320"
    df1 = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )
    df1 = px.scatter(
        df1, #this is the dataframe you are trying to plot
        x = "FIRST_TX",
        y = "UST_IN_SUM",
        color = "SUM_RANK",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df1)    





    query_id = "c96f0ab3-0f21-40bf-883a-90b566ed4320"
    df2 = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )
    df2 = px.scatter(
        df2, #this is the dataframe you are trying to plot
        x = "FIRST_TX",
        y = "UST_OUT_SUM",
        color = "SUM_RANK",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df2) 


    query_id = "c96f0ab3-0f21-40bf-883a-90b566ed4320"
    df3 = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )
    df3 = px.scatter(
        df3, #this is the dataframe you are trying to plot
        x = "FIRST_TX",
        y = "PROFIT_SUM",
        color = "SUM_RANK",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df3) 





    # ------------------------------------------------
# 	FIRST_TX	UST_IN_SUM	IN_TX	INN_AMT_AVG	INN_AMT_MED	UST_OUT_SUM	OUT_TX	OUT_AMT_AVG	OUT_AMT_MEDIAN	PROFIT_SUM	PROFIT_AVG	PROFIT_MEDIAN
# https://app.flipsidecrypto.com/velocity/queries/c96f0ab3-0f21-40bf-883a-90b566ed4320