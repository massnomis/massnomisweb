

import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("Levana Traits")

query_id = "a47c00d5-1052-4ec6-aa39-06a08f7a6742"
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
EGG
""")




st.dataframe(df)

query_id = "33397e50-6308-4b15-976a-811e19131433"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DUST
""")
st.dataframe(df)
query_id = "893c0575-c26d-4e5d-bd52-51762112edf7"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
METEOR
""")
st.dataframe(df)

