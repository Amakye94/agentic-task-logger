import streamlit as st
import requests

st.title("🚀 My First Agentic App")

if st.button("Click Me"):
    response = requests.post("http://backend:8000/log")
    
    if response.status_code == 200:
        st.success("Saved to backend 🎉")
    else:
        st.error("Something went wrong")