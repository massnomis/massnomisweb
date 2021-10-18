import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("YEET")

    query_id = "eb66ba08-c49b-4350-ab5a-ffd283231317"
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
        x = "DAYZ",
        y = ["ETHPREMIUMPCT","LUNAPREMIUMPCT"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    # DAYZ	ETHPRICE	PRICEBETH	ETHPREMIUM	ETHPREMIUMPCT	LUNAPRICE	PRICEBLUNA	LUNAPREMIUM	LUNAPREMIUMPCT
# https://app.flipsidecrypto.com/velocity/queries/eb66ba08-c49b-4350-ab5a-ffd283231317