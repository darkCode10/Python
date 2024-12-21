import streamlit as st
import pandas as pd 
import numpy as np

##Title for the document
st.title("Hello Streamlit")

##Disply a simple text
st.write("This is a simple text")

##Create a dataframe
df=pd.DataFrame({
    'First Column':[1,2,3,4],
    'Second Column':[10,20,30,40]
}) 

##Display the DataFrame
st.write("This is dataframe")
st.write(df)

##Create line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
