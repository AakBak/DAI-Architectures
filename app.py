import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Distributed AI Architectures", layout="wide")

with open("DAI.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=3000)