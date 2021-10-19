import plotly
import streamlit as st

import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json
def app():

    st.title("WElcome")
    st.write('list of everything here. what it is yada yada') # df, err, func, keras!
    st.title("Following Categories:")
    st.write('@massnomis') # df, err, func, keras!

    st.header('NFTs:')
    st.subheader('FLASHY')
    st.write('Opensea Volume Flash Bounty') 
    st.subheader('GPdata')
    st.write('Galactic Punks Data') 
    st.subheader('gpusers')
    st.write('Galactic Punks User Data') 



    st.header('Airdrop Activity:')
    st.subheader('loop1')
    st.write('Generalized LOOPR DATA') 
    st.subheader('loop2')
    st.write('Individualized LOOPR DATA') 
    

    st.header('Fees:')
    st.subheader('eth_fees')
    st.subheader('polygon_fees')

    st.header('Staking Prcing Data:')
    st.subheader('beth')
    st.subheader('bluna')

    st.header('Dex Data:')
    st.subheader('steth')
    st.subheader('eth_matic_vol')

    st.header('Money Market Data:')  
    st.subheader('aave_migration')
    st.subheader('polygon_fees')

    st.header('HOME and Garbage:')  
    st.subheader('home')
    st.subheader('extra')



