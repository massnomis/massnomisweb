import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json
query_id = input("api/query_id")
print("query_id" + query_id)
chart_type = input("chart_type")
print("chart_type" + chart_type)

query_id = query_id
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df)