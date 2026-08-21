import streamlit as st
import pandas as pd
import numpy as nd
import matplotlib.pyplot as plt
import plotly.express as px
import requests

st.title("Hello")
st.write("This is my 1st streamlit:streamlit:")
st.text("Lets get started")

name=st.text_input("Enter name:")
if st.button("Greets!"):
    st.success(f"Hello {name}! Mam")

    df = pd.DataFrame(nd.random.randn(10,2), columns=['A','B'])
    st.line_chart(df)
    st.bar_chart(df)

    st.image(r"C:\Users\misht\OneDrive\Pictures\Screenshots\Screenshot (285).png")
    upload_file=st.file_uploader("upload a csv.", type="csv")
    if upload_file:
        df = pd.read_csv(upload_file)
        st.dataframe(df)

st.sidebar.title("Navigation")
st.sidebar.subheader("About")

st.number_input("Enter ur marks", min_value=0, max_value=100)
st.slider("Choose ur rating",0,10)
st.text_area("Enter 300 words essay: ")
st.markdown("I am **Bold**, I am *italic*, I am 'code', I am link, [YCCE](https://ycce.mastersofterp.in/)")

st.code("for i in range(5): print(i)",language="python")
st.selectbox("select your Grade",["A","B","C"])
st.radio("Select ur grade",["aaj","kal","roj"])
st.multiselect("select your Grade",["Samosa","Sweet","Juice"])
st.checkbox("Agree to T&C")
option = st.radio("select your choice",["A","B","C"])

if option == "A":
    st.write("1 day holiday allowed")
if option == "B":
    st.write("2 day holiday allowed")
if option == "C":
     st.write("Fail-very dangerous")

with st.form("login form"):
          username = st.text_input("Enter username: ")
          password = st.text_input("Enter password: ")
          submitted = st.form_submit_button("Log in")

          if submitted:
               st.success(f"Welcome {username}!")

fig, ax=plt.subplots()
ax.plot([1,2,3],[1,4,9])
st.pyplot(fig)

df=px.data.iris()
fig=px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)