import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title of the app
st.title("📊 Simple Streamlit Web App")

# Sidebar
st.sidebar.header("App Controls")
user_name = st.sidebar.text_input("Enter your name", "Guest")

# Welcome message
st.write(f"👋 Welcome, **{user_name}**! This is a demo Streamlit app.")

# Generate some random data
st.subheader("Random Data Table")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['Column A', 'Column B', 'Column C']
)
st.dataframe(data)

# Plot the random data
st.subheader("Line Chart of Random Data")
fig, ax = plt.subplots()
data.plot(ax=ax)
st.pyplot(fig)

# Button example
if st.button("Say Hello"):
    st.success(f"Hello {user_name}, thanks for trying this demo!")
