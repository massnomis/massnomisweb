import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("LEVANA NFTs")

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/9bdc0745-9d56-4be2-8a56-b4ebcdb10a9a/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
METEORS, transactions per day, by rarity
""")


t_f = False
st.sidebar.write("Choose y-axis scale")
check = st.sidebar.checkbox("Linear/Log")
if check: 
    t_f = True

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "SUM(TXN_COUNT)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/9bdc0745-9d56-4be2-8a56-b4ebcdb10a9a/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
METEORS LUNA volume by rarity and day
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "SUM(TXN_VOLUME)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/9bdc0745-9d56-4be2-8a56-b4ebcdb10a9a/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
METEORS, average sale price, by day and rarity
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "AVG(TXN_AVG)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/9bdc0745-9d56-4be2-8a56-b4ebcdb10a9a/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
METEORS, median sale price, by day and rarity
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "MEDIAN(TXN_MEDIAN)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/9bdc0745-9d56-4be2-8a56-b4ebcdb10a9a/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
METEORS, FLOOR PRICE
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "MIN(FLOOR_PRICE)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/9bdc0745-9d56-4be2-8a56-b4ebcdb10a9a/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
METEORS, total sales by day and rarity
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "RUNNING_TX_COUNT_SUM",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/9bdc0745-9d56-4be2-8a56-b4ebcdb10a9a/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
METEORS, LUNA sum by rarity
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "RUNNING_VOLUME_SUM",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
# RUNNING_TX_COUNT_SUM
# RUNNING_VOLUME_SUM
# ------------------------
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/430c8cd3-2a0d-4367-8656-03978589b7f1/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
EGGS, total sales by day and rarity
""")



df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "SUM(TXN_COUNT)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/430c8cd3-2a0d-4367-8656-03978589b7f1/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
EGGS, daily LUNA sale volume by rarity
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "SUM(TXN_VOLUME)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/430c8cd3-2a0d-4367-8656-03978589b7f1/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
EGGS, average sale price by day and rarity
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "AVG(TXN_AVG)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/430c8cd3-2a0d-4367-8656-03978589b7f1/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
EGGS, median sale price by day and rarity
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "MEDIAN(TXN_MEDIAN)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/430c8cd3-2a0d-4367-8656-03978589b7f1/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
EGGS, FLOOR PRICE
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "MIN(FLOOR_PRICE)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/430c8cd3-2a0d-4367-8656-03978589b7f1/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
EGGS, total sales count by rarity
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "RUNNING_TX_COUNT_SUM",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/430c8cd3-2a0d-4367-8656-03978589b7f1/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
EGGS, LUNA running volume by rarity
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "RUNNING_VOLUME_SUM",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
# RUNNING_TX_COUNT_SUM
# RUNNING_VOLUME_SUM
# ----------------------
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7e5ed5f7-8195-4f1d-b20c-a77f464b28e9/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DUST, transaction count by rarity
""")



df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "SUM(TXN_COUNT)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)




df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7e5ed5f7-8195-4f1d-b20c-a77f464b28e9/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DUST LUNA VOLUME by day and rarity
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "SUM(TXN_VOLUME)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7e5ed5f7-8195-4f1d-b20c-a77f464b28e9/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DUST, average sale price, by day and rarity
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "AVG(TXN_AVG)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7e5ed5f7-8195-4f1d-b20c-a77f464b28e9/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DUST median sale price by day and rarity
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "MEDIAN(TXN_MEDIAN)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7e5ed5f7-8195-4f1d-b20c-a77f464b28e9/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DUST, floor ppice
""")

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "MIN(FLOOR_PRICE)",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7e5ed5f7-8195-4f1d-b20c-a77f464b28e9/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DUST, total sale count by day 
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "RUNNING_TX_COUNT_SUM",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7e5ed5f7-8195-4f1d-b20c-a77f464b28e9/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DUST, RUNNING LUNA SALES by rarity
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "RUNNING_VOLUME_SUM",
    color = "RARITY",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

# RUNNING_TX_COUNT_SUM
# RUNNING_VOLUME_SUM

# 9bdc0745-9d56-4be2-8a56-b4ebcdb10a9a
# day, RARITY, COL_NAME, sum(TXN_COUNT),	sum(TXN_VOLUME), 	avg(TXN_AVG), median(TXN_MEDIAN),	min(FLOOR_PRICE)
# METEORS

# 430c8cd3-2a0d-4367-8656-03978589b7f1
# day, RARITY, COL_NAME, sum(TXN_COUNT),	sum(TXN_VOLUME), 	avg(TXN_AVG), median(TXN_MEDIAN),	min(FLOOR_PRICE)
# EGG

# 7e5ed5f7-8195-4f1d-b20c-a77f464b28e9
# day, RARITY, COL_NAME, sum(TXN_COUNT),	sum(TXN_VOLUME), 	avg(TXN_AVG), median(TXN_MEDIAN),	min(FLOOR_PRICE)
# DUST


