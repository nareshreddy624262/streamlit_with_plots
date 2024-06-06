#import necessary librarys


import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sn
import matplotlib.pyplot as plt


data = pd.DataFrame(np.random.randn(50,3),columns=["column-1","column-2","column-3"])

st.header("working with plots in streamlit ...")
st.subheader("line chart through streamlit .")
st.line_chart(data)

st.subheader("bar-chart through streamlit..")
upload_file = st.file_uploader("uplaod your file here..",type = ["csv"])
file = pd.read_csv(upload_file)
if file is not None:
    st.subheader("dataframe for given data..")
    st.table(file.head())
    st.subheader("bar chart for above data...")
    st.bar_chart(file)
    st.subheader("line-chart for above data...")
    st.line_chart(file)
    st.subheader("area chart for above data ...")
    st.area_chart(file)
