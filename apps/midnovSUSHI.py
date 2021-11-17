import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
   


    query_id = "204a4d8f-b1eb-4149-aefe-4d42c0da8e62"
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
 

    




    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "WEEK",
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
    query_id = "204a4d8f-b1eb-4149-aefe-4d42c0da8e62"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "WEEK",
        y = "TX_COUNT",
        color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "1. Active Weekly Users - TX count",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    query_id = "81b05fe3-5951-4c4c-91ae-b4a8fa20e5b8"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "MONTH",
        y = "USD_MONTH_SUM",
        color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "2.  Monthly Swap Volume",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    query_id = "81b05fe3-5951-4c4c-91ae-b4a8fa20e5b8"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "MONTH",
        y = "MONTH_AVERAGE_USD",
        color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "2.  Monthly Swap Volume-avg swap size",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    query_id = "81b05fe3-5951-4c4c-91ae-b4a8fa20e5b8"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "MONTH",
        y = "TX_COUNT",
        color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "2.  Monthly Swap Volume-TX_COUNT",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)



    # # #4 User Journey and Outflows
    # st.plotly_chart(df)
    # query_id = "81b05fe3-5951-4c4c-91ae-b4a8fa20e5b8"
    # df = pd.read_json(
    #     f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    # convert_dates=["TIMESTAMP_NTZ"],
    # )  
    # df = px.scatter(
    #     df, #this is the dataframe you are trying to plot
    #     x = "MONTH",
    #     y = "TX_COUNT",
    #     color = "UNI_VS_SUSHI",
    #     orientation = "v",
    #     title = "4. User Journey and Outflows",
    #     template = "plotly_white",
    #     width = 1000,
    #     height = 600,
    #     log_y = t_f
    # )
    # st.plotly_chart(df)
    # MONTH_AVERAGE_USD
# MONTH	UNI_VS_SUSHI	USD_MONTH_SUM	MONTH_AVERAGE_USD
    # df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/81b05fe3-5951-4c4c-91ae-b4a8fa20e5b8/data/latest')
    # df = px.bar(
    #     df, #this is the dataframe you are trying to plot
    #     x = "MONTH",
    #     y = ["USD_MONTH_SUM","MONTH_AVERAGE_USD"],
    #     color = "UNI_VS_SUSHI",
    #     orientation = "v",
    #     title = "Monthly Swap Volume",      
    #     template = "plotly_white",
    #     width = 1000,
    #     height = 600,
    #     log_y = t_f
    # )
    # st.plotly_chart(df)   
    query_id = "a0695433-8ff4-4076-8206-361da8d6785f"
 
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "ADDRESS_COUNT",
        color = "PLATFORM",
        orientation = "v",
        title = "4. User Journey and Outflows, users per platform",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    query_id = "a0695433-8ff4-4076-8206-361da8d6785f"
 
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "AVERAGE_FEE_USD",
        # color = "PLATFORM",
        orientation = "v",
        title = "4. User Journey and Outflows - average gas fee",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    # WEEK	UNI_VS_SUSHI	USD_MONTH_SUM	FROMM	TX_COUNT	MONTH_AVERAGE_USD
# # DHOUR	COUNT(POOL_NAME)	POOL_NAME
# DAY	ADDRESS_COUNT	PLATFORM	FEE_DAY	AVERAGE_FEE_USD
# 204a4d8f-b1eb-4149-aefe-4d42c0da8e62