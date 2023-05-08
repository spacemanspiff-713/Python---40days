import streamlit as st
import pandas

df = pandas.read_csv("data.csv", sep=",")
df_topics = pandas.read_csv("topics.csv", sep=",")

print(f"THIS IS DATA {df}")
print(f"THIS IS TOPICS {df_topics}")

st.set_page_config(layout="wide")
st.title("The Best Company")
st.write("Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate impedit pariatur quidem, reprehenderit nostrum illo est magni unde at cum delectus voluptatum doloribus voluptatibus. Ipsum, doloribus odit? In dolorum provident animi veritatis, adipisci dolorem ipsa harum officiis nihil eaque incidunt quod, consectetur quasi perferendis ipsum ea minus iusto deleniti quas!")
st.subheader("Our Team")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role'].capitalize()}")
        st.image("images/" + row["image"])
        st.write("---")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role'].capitalize()}")
        st.image("images/" + row["image"])
        st.write("---")

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role'].capitalize()}")
        st.image("images/" + row["image"])
        st.write("---")