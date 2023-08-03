import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Iain Derrett")
    content = """
    Hi, I am Iain! I am a civil engineer who is starting a journey to self-learn the skills necessary to become a DevOps engineer.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)
