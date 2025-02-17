import  streamlit as st
import plotly.express as px
import pandas

df = pandas.read_csv("data.txt")
st.write(df.head())

figure = px.line(x=df["date"], y=df["temperature"],
                                labels={"date": "Date", "temperature":"Temperature (C)"})


st.plotly_chart(figure)