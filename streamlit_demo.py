import streamlit as st
import pandas as pd
import numpy as np

st.title('Charts demo')

df_map = pd.DataFrame(
     np.random.randn(100, 2) / [50, 50] + [48.30639, 14.28611],
     columns=['lat', 'lon'])

df = pd.DataFrame(np.random.randn(10, 5),
  columns = ('col %d' % i
    for i in range(5)))


SEL_MAP = "Map"
SEL_LINE_PLOT = "Line plot"
SEL_BAR_PLOT = "Bar plot"


st.sidebar.title("Options")

plot_to_show = st.sidebar.selectbox(
    "Which chart do you want to see?",
    (SEL_MAP, SEL_LINE_PLOT, SEL_BAR_PLOT)
)


if plot_to_show == SEL_MAP:
  st.header("Map with markers")
  st.map(df_map)
elif plot_to_show == SEL_LINE_PLOT:
  st.header("Line chart")
  st.line_chart(df)
elif plot_to_show == SEL_BAR_PLOT:
  st.header("Bar chart")
  st.bar_chart(df)
