import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("1. [Easy] Daily Reward Distribution")

    query_id = "58ce4e69-1761-4ce0-8305-4d8c4a35c194"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)


    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    


    st.markdown("""
    """)
    

    


    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = ["REWARDS"],
        color = "POOL_NAME",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)


    st.title("2. [Easy]Volume of THORChain Activity by Asset ")

    
    query_id = "b0bd3376-90e0-4ffd-8f33-4c203b891ad1"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DDATE",
        y = ["SUM(RUNE_AMOUNT)"],
        color = "BURN_ASSET",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)





    st.title("3. [Easy] Number of Users of THORChain Bridges by Asset")

    
    query_id = "1bdf164a-aa2d-4b85-b165-83883fa4ec1b"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DDATE",
        y = ["ADD_COUNT"],
        color = "BURN_ASSET",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    st.title("4. [Easy] Total volume swapped by pool and over time")

    
    query_id = "a7c80981-724c-4196-a863-db8b7d3a9047"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = ["SUM(TO_AMOUNT_MIN_USD)"],
        color = "POOL_NAME",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)



    st.title("5. [Easy] Swapping")

    
    query_id = "7a2c77bb-ca33-41cf-b002-2a8c147dcfc6"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = ["SWAP_VOLUME"],
        color = "POOL_NAME",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    query_id = "7a2c77bb-ca33-41cf-b002-2a8c147dcfc6"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)


    st.title("6. [Easy] Number of LPs")

    
    query_id = "fa713bcb-00ba-41ee-ada7-b0001a7b1776"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYS",
        y = ["COUNT(DISTINCT(FROM_ADDRESS))"],
        color = "POOL_NAME",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)



    st.title("7. [Hard] Weekly APY")

    
    query_id = "8f18dd2c-06c0-4ad9-b7d5-acddef7f198f"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = ["APY_NODE_OPS","APY_LPS"],
        # color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)



    st.title("8. [Hard] Trading by time")

    
    query_id = "ef0b2fd1-e03c-4e64-8db3-8c236c59ff9d"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "DHOUR",
        y = ["COUNT(POOL_NAME)"],
        color = "POOL_NAME",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    st.title("9. [Hard] RUNE price vs Swapper activity")

    
    query_id = "4ef88898-00e1-4596-9750-81d65c26b7e4"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = ["VOLSUM"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    
    query_id = "4ef88898-00e1-4596-9750-81d65c26b7e4"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = ["RUNEP"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    
    query_id = "4ef88898-00e1-4596-9750-81d65c26b7e4"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAY",
        y = ["VOLSUM/RUNEP"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)


    st.title("FREE EXTRA SWAPS BY CHAIN")

    
    query_id = "e85b23cb-141f-420a-ab35-2bd0e78c8694"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = ["COUNT(DISTINCT(TX_ID))","COUNT(DISTINCT(FROM_ADDRESS))","COUNT(DISTINCT(TO_ADDRESS))"],
        color = "BLOCKCHAIN",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    # DAYZ
    # BLOCKCHAIN	
    # COUNT(DISTINCT(TX_ID) )
    # COUNT(DISTINCT(FROM_ADDRESS))	
    # COUNT(DISTINCT(TO_ADDRESS))