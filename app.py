import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.title("This is my streamlit app")

if st.button("Click me please"):
    st.balloons()
    st.snow()


lower_bound, higher_bound = st.slider('choose range to plot', min_value=-10, max_value=10, value=(-5, 5))

def plot_x2(lower_bound, higher_bound):
    x = np.arange(lower_bound,higher_bound)
    y = x**2
    fig=plt.figure(figsize=(12,6))
    plt.plot(x,y)
    return fig

st.pyplot(plot_x2(lower_bound, higher_bound))


txt = st.text_input("Type here")

st.text(txt)

# df = px.data.iris()

# fig = px.scatter(df, x="sepal_width", y="sepal_length", 
#                 color="species", size='petal_length', 
#                 hover_data=['petal_width'])

# st.plotly_chart(fig)

st.page_link('pages/plotly_chart.py')