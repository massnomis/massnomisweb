import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("MEGA TERRA NFT")

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/39fcd840-cbc6-4ca1-bb48-833f806ec845/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------


st.dataframe(df)

st.markdown("""
TX COUNT by PROJECT
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

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/39fcd840-cbc6-4ca1-bb48-833f806ec845/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
DAILY LUNA VOLUME BY PROJECT
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

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/39fcd840-cbc6-4ca1-bb48-833f806ec845/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
DAILY LUNA VOLUME BY PLATFORM

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

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/39fcd840-cbc6-4ca1-bb48-833f806ec845/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
DAILY TX COUNT BY PLATFORM

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

st.markdown("""
CHOOSE YOUR OWN ADVENTURE!!
""")

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/39fcd840-cbc6-4ca1-bb48-833f806ec845/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)
my_slider_val = st.slider('slider is project rank', 1, 96)
st.write(my_slider_val)
df_new = df[df["PROJECT_RANK"] == my_slider_val]

linechart = px.scatter(
    df_new,
    x="DAY",
    y=["TXN_VOLUME"],
    color="COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600 
)
st.plotly_chart(linechart, use_container_width=False)



linechart = px.scatter(
    df_new,
    x="DAY",
    y=["TXN_COUNT"],
    color="COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600
)
st.plotly_chart(linechart, use_container_width=False)



df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/8a793b94-dfc4-4673-8ea6-0dd69bde9f06/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
IT ALL COMES BACK TO THE LUNA PRICE
""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DATE",
    y = "LUNA_PRICE",
# color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600
)
# ,"TXN_VOLUME"]
st.plotly_chart(df)
