import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import time


st.title("This is my streamlit app")

st.write("---")

if st.button("Release ballons in the air"):
    progress_text = "Inflating ballons. Please wait..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.balloons()


st.write("---")

st.text("Visualize y=x**2 function")

lower_bound, higher_bound = st.slider('choose range to plot', min_value=-10, max_value=10, value=(-5, 5))

def plot_x2(lower_bound, higher_bound):
    x = np.arange(lower_bound,higher_bound)
    y = x**2
    fig=plt.figure(figsize=(12,6))
    plt.plot(x,y)
    return fig

st.pyplot(plot_x2(lower_bound, higher_bound))

st.write("---")

txt = st.text_input("Type here")
st.text(txt)

st.write("---")

st.page_link('pages/plotly_chart.py', label='Iris graph', icon="🌸")
