

import plotly
import streamlit as st
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("WHO DO MINE stakers delegate to?")

    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/420b2ed2-3e6f-40f3-b36c-bb686ef3777d/data/latest')



    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    

    st.dataframe(df)

    st.markdown("""
    """)
    



    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "VALIDATOR_ADDRESS_LABEL",
        y = "SUM(EVENT_AMOUNT)",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df)


    df2 = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/63898d7d-4a3f-45e0-93cf-8411dd1a14fc/data/latest')

    st.title("WHERE DOes EVREYONE ELSE delegate to?")


    df2 = px.bar(
        df2, #this is the dataframe you are trying to plot
        x = "VALIDATOR_ADDRESS_LABEL",
        y = "SUM(EVENT_AMOUNT)",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df2)



# https://api.flipsidecrypto.com/api/v2/queries/420b2ed2-3e6f-40f3-b36c-bb686ef3777d/data/latest
# VALIDATOR_ADDRESS_LABEL	SUM(EVENT_AMOUNT)



# https://api.flipsidecrypto.com/api/v2/queries/63898d7d-4a3f-45e0-93cf-8411dd1a14fc/data/latest
# not
# VALIDATOR_ADDRESS_LABEL	SUM(EVENT_AMOUNT)