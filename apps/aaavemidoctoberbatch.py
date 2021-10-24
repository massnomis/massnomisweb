import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("24. [Easy] Unique Addresses")

    query_id = "072b7018-c632-444b-a263-5f09d02b1cc3"
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
    

    
#aaavemidoctoberbatch

    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = ["DEPOSITORS","WITHDRAWERS","BORROWERS","REPAYERS"],
        # color = "POOL_NAME",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
# DAYZ	DEPOSITORS	WITHDRAWERS	BORROWERS	REPAYERS

    st.title("25. [Hard] Most Popular COMBOS  -- comp")

    
    query_id = "c859c36b-ca8f-4fa4-ba5b-09744c7b6e2b"
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





    st.title("25. [Hard] Most Popular COMBOS  -- aave")

    
    query_id = "9f901ec4-4da3-4283-a312-e81fec52e505"
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

    st.title("26. [Hard] Whale Activities (besides having diamond hand) comp")

    
    query_id = "d017baf7-a5e2-43f9-9bd2-3676c98fc337"
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



    st.title("26. [Hard] Whale Activities (besides having diamond hand) aave")

    
    query_id = "fe7ec729-41c2-4097-a34e-9be3ed78b390"
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

