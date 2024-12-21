import streamlit as st
import pandas as pd
st.title("Streamlit Input Text")

name=st.text_input("Enter Your Name")
if name:
    st.write(f"Hello, {name}")

age=st.slider("Select your age:",1,100,20)
st.write(f"Your age is {age}")

options=["Pyhton","C++","Java","Javascript"]
choice=st.selectbox("Choose your favorite programming language:",options)
st.write(f"You selected {choice}")

data={
    "Name":["Ahsaan Thakur","Hashir Sexy","Mannan Chilgoza","Hannan TLP","Shawaal Emergency"],
    "Age":[22,22,21,40,22],
    "Salary":["$15000","$18000","$55000","2 Bananas","Nancy"]
}
df=pd.DataFrame(data)
df.to_csv("SampleData.csv")
uploaded_file=st.file_uploader("Choose CSV File",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)