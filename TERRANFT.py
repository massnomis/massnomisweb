import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("MEGA TERRA NFT")

query_id = "594332b2-ccac-4b9c-b0cb-12875234fc4c"
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/594332b2-ccac-4b9c-b0cb-12875234fc4c/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------


st.dataframe(df)

st.markdown("""
""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "TXN_COUNT",
    color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600
)
st.plotly_chart(df)

query_id = "594332b2-ccac-4b9c-b0cb-12875234fc4c"
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/594332b2-ccac-4b9c-b0cb-12875234fc4c/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "TXN_VOLUME",
    color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600
)
st.plotly_chart(df)

query_id = "594332b2-ccac-4b9c-b0cb-12875234fc4c"
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/594332b2-ccac-4b9c-b0cb-12875234fc4c/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "TXN_VOLUME",
    color = "PLATFORM",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600
)
st.plotly_chart(df)
query_id = "594332b2-ccac-4b9c-b0cb-12875234fc4c"
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/594332b2-ccac-4b9c-b0cb-12875234fc4c/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "TXN_COUNT",
    color = "PLATFORM",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600
)
st.plotly_chart(df)

# ,"TXN_VOLUME"]