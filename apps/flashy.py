import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json


st.set_page_config(layout="wide")
st.title("MEGA FLASH NFT")
st.markdown(
    """
    maybe you came from flipside, maybe not, but lemme help you out.
    """
)
st.title('First')
st.header('We')
st.subheader('Start')
st.text('With all Labeled NFT projects on opensea and rank them by total volume LOOK PLZ')


query_id = "9e88832f-c075-4b7e-a871-63d4852372ee"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)  

st.write(df)
st.title('But..')
linechart = px.bar(
    df,
    x="DAY",
    y=["USD_VOLUME"],
    color="PROJECT_NAME" 
)

st.plotly_chart(linechart, use_container_width=True)
st.header('We see that combined they are hard to read')

linechart = px.line(
    df,
    x="DAY",
    y=["USD_VOLUME"],
    color="PROJECT_NAME" 
)

st.plotly_chart(linechart, use_container_width=True)

st.text('So we need to come up with a way to see just one or two projects')

linechart = px.scatter(
    df,
    x="DAY",
    y=["USD_VOLUME"],
    color="PROJECT_NAME" 
)

st.plotly_chart(linechart, use_container_width=True)

st.subheader('A WILD SLIDER APPEREAD!!')

my_slider_val = st.slider('slider is project rank', 1, 1035)
st.write(my_slider_val)
df_new = df[df["PROJECT_RANK"] == my_slider_val]

linechart = px.line(
    df_new,
    x="DAY",
    y=["USD_VOLUME"],
    color="PROJECT_NAME" 
)

st.plotly_chart(linechart, use_container_width=True)

st.subheader('ALL COMES BACK TO ETH...')



# ,
# linechart = px.line(
#     df,
#     x="DAY",
#     y=["ETH_VOLUME"],
#     color="my_slider_val" 
# )

# st.plotly_chart(linechart, use_container_width=True) 

linechart = px.line(
    df,
    x="DAY",
    y=["ETH_PRICE"],
    # color="PROJECT_NAME"  
)

st.plotly_chart(linechart, use_container_width=True)


st.subheader('https://app.flipsidecrypto.com/dashboard/woah-you-can-download-as-csv-by-clicking-the-three-dots-aBpE5F')
st.code('have a good one')

# for i in range(int(st.number_input('Num:'))): foo()
# if st.sidebar.selectbox('I:',['f']) == 'f': b()
# my_slider_val = st.slider('Quinn Mallory', 1, 88)
# st.write(slider_val)




# st.selectbox('Select', [1,2,3])
# st.multiselect('Multiselect', [1,2,3])
# st.slider('Slide me', min_value=0, max_value=10)