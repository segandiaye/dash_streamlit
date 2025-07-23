import streamlit as st
import plotly.express as px
from streamlit_extras.let_it_rain import rain

rain(
    emoji="🌸",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
    )

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", 
                color="species", size='petal_length', 
                hover_data=['petal_width'])

st.plotly_chart(fig)