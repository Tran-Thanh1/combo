# importing Necessary Libraries
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
# Defining random Values for Chart
df = pd.DataFrame(
np.random.randn(10, 2),
columns=['a', 'b'])
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
x='a', y='b', tooltip=['a', 'b'])
# Defining Chart in write() function
st.write(chart)
