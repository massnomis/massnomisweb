import streamlit as st
import file3.py
app = MultiApp()
st.set_page_config(layout="wide")
st.markdown("""
# 
""")
from apps import file1.py

app.add_app("file1.py",file1.py.app)