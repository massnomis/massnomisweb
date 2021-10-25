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
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "TO_ADDRESS_NAME",
        y = ["TOTAL_AMOUNT"],
        color = "SYMBOL",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    query_id = "c859c36b-ca8f-4fa4-ba5b-09744c7b6e2b"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "TO_LABEL",
        y = ["TOTAL_AMOUNT"],
        color = "SYMBOL",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)


# TOTAL_AMOUNT	SYMBOL
# 
# TO_ADDRESS_NAME	TO_LABEL

    st.title("25. [Hard] Most Popular COMBOS  -- aave")

    
    query_id = "9f901ec4-4da3-4283-a312-e81fec52e505"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "TO_ADDRESS_NAME",
        y = ["TOTAL_AMOUNT"],
        color = "SYMBOL",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    query_id = "9f901ec4-4da3-4283-a312-e81fec52e505"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "TO_LABEL",
        y = ["TOTAL_AMOUNT"],
        color = "SYMBOL",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
# TOTAL_AMOUNT	SYMBOL
# 
# TO_ADDRESS_NAME	TO_LABEL
    st.title("26. [Hard] Whale Activities (besides having diamond hand) comp")

    
    query_id = "8cf94345-0083-45b8-8991-8c25b452cd42"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter_3d(
        df, #this is the dataframe you are trying to plot
        x = "WHALE_NUMBER",
        y = "PCT_LOAN_REPAYED",
        z = "AGGREGATED_LOAN_AMOUNT",
        # orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

# WHALE_NUMBER	
# 	AGGREGATED_LOAN_AMOUNT	
# PCT_LOAN_REPAYED

    st.title("26. [Hard] Whale Activities (besides having diamond hand) aave")

    
    query_id = "74387ded-bd97-42e8-82e4-809dd7db03e8"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter_3d(
        df, #this is the dataframe you are trying to plot
        x = "WHALE_NUMBERZ",
        y = "PCT_LOAN_REPAYED",
        z = "AGGREGATED_LOAN_AMOUNT",
        # orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
	

    st.title("WHALE REPAYMENT TREND aave")

    
    query_id = "24660e5d-2047-4da7-8039-f087b8af2a5f"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DS",
        y = ["REPAYMENT_RATE"],
        # color = "AGGREGATED_LOAN_AMOUNT",
        # orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    # 24660e5d-2047-4da7-8039-f087b8af2a5f