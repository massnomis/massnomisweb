import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("ANGELS NEW YEARS")

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/0de27bfb-778d-4c28-8049-03097b9ff623/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
""")


t_f = False
st.sidebar.write("Choose y-axis scale")
check = st.sidebar.checkbox("Linear/Log")
if check: 
    t_f = True

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZZZ",
    y = "RUNNING_LUNA_USD",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/0de27bfb-778d-4c28-8049-03097b9ff623/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
""")



df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZZZ",
    y = "DAILY_NET_LUNA",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/0de27bfb-778d-4c28-8049-03097b9ff623/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
""")



df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZZZ",
    y = ["RUNNING_LUNA","RUNNING_LUNA_OUT"],
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
# 123312
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/0de27bfb-778d-4c28-8049-03097b9ff623/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
""")



df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZZZ",
    y = ["RUNNING_LUNA_USD","RUNNING_LUNA_OUT_USD"],
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/0de27bfb-778d-4c28-8049-03097b9ff623/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
""")



df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "COMISH_DAYZZ",
    y = "COMISH_USD",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/0de27bfb-778d-4c28-8049-03097b9ff623/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
""")



df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "COMISH_DAYZZ",
    y = "RUNNING_COMISH",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
# 0de27bfb-778d-4c28-8049-03097b9ff623

# DAYZZZ	LUNA_IN_TODAY	LUNA_IN_TODAY_USD	RUNNING_LUNA
# 	RUNNING_LUNA_USD	LUNA_OUT	LUNA_OUT_USD	DAILY_NET_LUNA	DAILY_NET_LUNA_USD	RUNNING_LUNA_OUT	RUNNING_LUNA_OUT_USD	COMISH_DAYZZ	COMISH_USD	RUNNING_COMISH