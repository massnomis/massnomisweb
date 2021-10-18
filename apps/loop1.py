import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("YEET")

    query_id = "a0f06e6e-9b8c-44f2-9934-25a6e6e0801b"
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
        x = "LAST_CLAIMED",
        y = "NET_STAKED",
        color = "CLAIMER",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df)

    # ------------------------------------------------

# LAST_CLAIMED	CLAIMER	LAST_CLAIMED_AMOUNT	TOTAL_CLAIMED_AMOUNT	MIN_STAGE	MAX_STAGE	AMOUNT_STAKED	AMOUNT_UNSTAKED	NET_STAKED	PCT_STAKED_LAST	BUY_AMOUNT	SELL_AMOUNT	NET_BOUGHT	PCT_BOUGHT_LAST	TRANSFER_IN	TRANSFER_OUT	NET_IN	PCT_TRANSFER_LAST
# https://app.flipsidecrypto.com/velocity/queries/a0f06e6e-9b8c-44f2-9934-25a6e6e0801b