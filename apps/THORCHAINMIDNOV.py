import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
   


    query_id = "da1daba5-4203-4275-81aa-c493ff0a263e"
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



    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "ASSET",
        y = "USERS",
        # color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "ON RAMP",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    
    query_id = "43394653-19ab-4b48-a210-8f8315647b47"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  


    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "ASSET",
        y = "USERS",
        # color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "OFF RAMP",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    st.plotly_chart(df)
    query_id = "44b209b9-d197-4b3b-b5eb-328a1db2b8fd"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "BLOCK_DAY",
        y = "N_ADDRESS",
        color = "POOL_NAME",
        orientation = "v",
        title = "POOL DEPTH",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    query_id = "caf3553f-a355-415d-8d02-15ba7d4e48d6"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "BLOCK",
        y = "COUNT(ADDRESS)",
        # color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "Wealth distribution",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    query_id = "af058a7c-28d4-4ecd-b27d-3e1e9b782f0a"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "BLOCK_DAY",
        y = "N_ADDRESS",
        color = "POOL_NAME",
        orientation = "v",
        title = "Whale activity",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)



    query_id = "f03794f4-8c19-4265-b00e-6f8939d5dc09"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    st.write(df)

    query_id = "9a1ba97b-9286-40ff-8060-437abd56cca8"
 
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "ADD_LIQUIDITY_COUNT_BY_DAY",
        # color = "PLATFORM",
        orientation = "v",
        title = "Liquidity In",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    query_id = "9a1ba97b-9286-40ff-8060-437abd56cca8"
 
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "USD_ADDED_FOR_DAY",
        # color = "PLATFORM",
        orientation = "v",
        title = "Liquidity In",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    # DAY	ADD_LIQUIDITY_COUNT_BY_DAY	USD_ADDED_FOR_DAY
    query_id = "ac5c6316-bd12-4186-b456-d5c1486f209d"
 
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "REMOVE_LIQUIDITY_COUNT_BY_DAY",
        # color = "PLATFORM",
        orientation = "v",
        title = "Liq Remove",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    query_id = "ac5c6316-bd12-4186-b456-d5c1486f209d"
 
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = "USD_REMOVED_FOR_DAY",
        # color = "PLATFORM",
        orientation = "v",
        title = "Liq Remove",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
# DAY	REMOVE_LIQUIDITY_COUNT_BY_DAY	USD_REMOVED_FOR_DAY



