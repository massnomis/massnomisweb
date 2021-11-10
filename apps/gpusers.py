
import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("GALACTIC PUNKS, THE WHO")

    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)


    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    

    st.dataframe(df)

    st.markdown("""Instead of Rendering every user a different color, I gave each user a ranked number, based on the total amount of LUNA spent interacting with GP contracts.

    """)
    # st.selectbox('Select', [1,2,3])



    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = "SUM",
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    st.subheader('Plotting the total amount of LUNA spent versus the individuals first interaction, we actually see a significant amount of users who spend very little within the first batch of interactions (first hour, less than 10 LUNA)')



    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = "AVG_Value_Z_Score_(Skew)",
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    st.subheader('Next is the skew, or where the user spends per tx relative to other users. This turned out to be a little more random than I thought, which is good for a fair launch.')

    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = ["AVG"],
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)  
    st.subheader('Average amount spent per tx seems to really rise at around 24 into the launch, dropping to 50 LUNA within 4 days. The largest spenders came in late on October 7th, roughly 48 hours after launch.')

    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = ["Median"],
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)  
    st.subheader('Median, which is hard to differentiate from the average, shows that early users spent less on average, also spent less on median. Those who knew the game made out the best.')

# ,"Median"
    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = ["tx_countz"],
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)   
    st.subheader('Number of transactions vs First tx shows us that the whales knew what was going on from the beginning, meaning that this was a well executed, fair launch of JPEG. NICE!')

# USERZ	SUM_RANK	user	
# first_interaction	tx_countz	
# SUM	AVG	Median	
# STD DEV	Z_P1	Z_N1	
# AVG_Value_Z_Score_(Skew)


    # ------------------------------------------------
