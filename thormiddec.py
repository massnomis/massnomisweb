import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("THOR MID DEC")

query_id = "bc3fd76c-5e84-4b77-9575-8e883da90a91"
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



st.markdown("""
LP RANK, POOLS AND ACTIONS""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "RANK",
    y = "POOLZ",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



query_id = "bc3fd76c-5e84-4b77-9575-8e883da90a91"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
THOR ACTIONS""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "RANK",
    y = "LP_ACTIONS",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)




query_id = "02c1a44e-f003-4a43-92b3-da6d17c1bc88"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
RUN, XRUNE, THOR Prices
""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "HOURZ",
    y = ["RUNE_PRICE","THOR_PRICE","XRUNE_PRICE"],
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

