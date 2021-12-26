import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("")

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/98446ff3-2cdb-4c11-b491-22e39b104896/data/latest",
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
    x = "DAY",
    y = "TXN_COUNT",
    color = "PLATFORM",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/98446ff3-2cdb-4c11-b491-22e39b104896/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
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
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/98446ff3-2cdb-4c11-b491-22e39b104896/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
st.markdown("""
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "TXN_AVG",
    color = "PLATFORM",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/98446ff3-2cdb-4c11-b491-22e39b104896/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
st.markdown("""
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "TXN_MEDIAN",
    color = "PLATFORM",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/98446ff3-2cdb-4c11-b491-22e39b104896/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
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
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/98446ff3-2cdb-4c11-b491-22e39b104896/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
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
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/98446ff3-2cdb-4c11-b491-22e39b104896/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
st.markdown("""
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "TXN_AVG",
    color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/98446ff3-2cdb-4c11-b491-22e39b104896/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
st.markdown("""
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "TXN_MEDIAN",
    color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)




# 98446ff3-2cdb-4c11-b491-22e39b104896
# PLATFORM	DAY	COL_NAME	TXN_COUNT	TXN_VOLUME	TXN_AVG	TXN_MEDIAN