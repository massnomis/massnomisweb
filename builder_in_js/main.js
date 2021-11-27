//package to create text document
fs = require('fs');

//variables of the python script
const prompt = require('prompt-sync')();
const id = prompt('Paste Query ID:');
const title = prompt('Title:');
const x = prompt('X Value:');
const y = prompt('Y Value:');

//python script code template
code = `import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():
    st.title("${title}")

    query_id = "${id}"
    df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/${id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )


    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    

    st.dataframe(df)

    st.markdown("""
    """)
    

    


    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "${x}",
        y = "${y}",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

loop



`

//print template
fs.writeFile(`${title}.txt`, code, function(err) {
    if (err) return console.log(err);
    console.log('done');
});