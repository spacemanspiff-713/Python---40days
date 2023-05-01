import streamlit as st

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