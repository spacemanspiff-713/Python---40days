import streamlit as st
import pandas

df = pandas.read_csv("data.csv", sep=";")

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/profile-pic.png")

with col2:
    st.title("Jason Trimble")
    content = """
    Hello, World! I'm Jason, a python developer. Check out my projects and reach out to discuss partnering together for any projects you have in mind.
    """
    st.info(content)

contact_info = "Below you can find my current projects 👇🏼"

st.write(contact_info)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")