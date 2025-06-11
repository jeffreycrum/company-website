import streamlit as st
import pandas

st.header("The Best Company")

company_desc = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(company_desc)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv", sep=",")
thirds = len(df) // 3
print(thirds)
with col1:
    for index, row in df[:thirds].iterrows():
        full_name = f"{row['first name']} {row['last name']}"
        st.subheader(full_name.title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[thirds:-thirds].iterrows():
        full_name = f"{row['first name']} {row['last name']}"
        st.subheader(full_name.title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[-thirds:].iterrows():
        full_name = f"{row['first name']} {row['last name']}"
        st.subheader(full_name.capitalize())
        st.write(row['role'])
        st.image(f"images/{row['image']}")
