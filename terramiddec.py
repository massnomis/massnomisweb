import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("LUNA mid december")

query_id = "f51322fd-f7c9-44d5-8236-eaafd4993264"
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
""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "RANK",
    orientation = "v",
    color = "LABEL",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


query_id = "f51322fd-f7c9-44d5-8236-eaafd4993264"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
RANK VALIDATORS""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = "VOTING_POWER_AVERAGE",
    orientation = "v",
    color = "LABEL",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


query_id = "ad9e5e40-09f9-4978-85fa-9c109708fd60"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
nft terra1""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DATES",
    y = "NUMBER_OF_TRANSACTIONS",
    orientation = "v",
    # color = "LABEL",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

query_id = "ad9e5e40-09f9-4978-85fa-9c109708fd60"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
nft terra1""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DATES",
    y = "DAILY_VOLUME_IN_LUNA",
    orientation = "v",
    # color = "LABEL",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

query_id = "ad9e5e40-09f9-4978-85fa-9c109708fd60"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
nft terra1""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DATES",
    y = ["AVERAGE_PRICE_IN_LUNA","MAXIMUM_PRICE_IN_LUNA"],
    orientation = "v",
    # color = "LABEL",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

query_id = "558b7322-be3c-400f-84ed-11b10bbb57fd"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
nft terra2""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "PRICE",
    orientation = "v",
    color = "MARKET",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

query_id = "558b7322-be3c-400f-84ed-11b10bbb57fd"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
nft terra2""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "TXS",
    orientation = "v",
    color = "MARKET",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

query_id = "c154897e-8cdb-4c37-9e08-80a473e84df0"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
bluna1""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "START OF SLICE",
    y = "RATIO",
    orientation = "v",
    # color = "MARKET",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

query_id = "c154897e-8cdb-4c37-9e08-80a473e84df0"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
bluna1""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "START OF SLICE",
    y = "BLUNA_AMOUNT",
    orientation = "v",
    # color = "MARKET",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
query_id = "c154897e-8cdb-4c37-9e08-80a473e84df0"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
bluna1""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "START OF SLICE",
    y = "LUNA_AMOUNT",
    orientation = "v",
    # color = "MARKET",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


query_id = "309d7022-d308-4d29-8a3a-4a255ee6a723"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
bluna2""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = ["LUNAPRICE","PRICEBLUNA"],
    orientation = "v",
    # color = "MARKET",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


query_id = "309d7022-d308-4d29-8a3a-4a255ee6a723"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
bluna2""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = ["LUNAPREMIUM", "LUNAPREMIUMPCT"],
    orientation = "v",
    # color = "MARKET",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

# 309d7022-d308-4d29-8a3a-4a255ee6a723
# DAYZ	LUNAPRICE	PRICEBLUNA	LUNAPREMIUM	LUNAPREMIUMPCT
# bluna2