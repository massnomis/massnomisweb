import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json


#st.set_page_config(layout="wide")
st.title("BLOCK_TIMESTAMP	TX_ID	Owner	TOKENID")

query_id = "e585c27c-28eb-4b35-be6b-388913c373e0"
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





df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "BLOCK_TIMESTAMP",
    y = ["TOKENID"],
    color = "Owner",
    # orientation = "v",
    # template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
st.subheader('')

st.title("Owners, Meteors, Dust, Eggs")


query_id = "e20a7969-95d3-47ad-9531-fe6e29d557e3"
df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
df = px.scatter_3d(
    df, #this is the dataframe you are trying to plot
    x = "METEORS",
    y = "DUST",
    z = "EGGS",
    color = "OWNER",
    # orientation = "v",
    # template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

st.subheader('')


