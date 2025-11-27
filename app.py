import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import time
import app1
import app2
import app3
img = Image.open('images/icon1.png')
img1 = Image.open('images/icon.png')
img2 = Image.open('images/icon1.jpg')
st.set_page_config(page_title="DigiLab", page_icon=img2, layout="wide")
hide_stream_lit_style = """<style>#MainMenu{visibility: hidden;} footer {visibility: hidden}</style>"""
st.markdown(hide_stream_lit_style, unsafe_allow_html=True)

PAGES = {
    "Home": app1,
    "Visualization": app2,
    "Prediction": app3
}
st.sidebar.image(img, width=120)
st.sidebar.subheader('Welcome')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
y = st.spinner(f'Loading {selection} ...')

with y:
    time.sleep(0.2)
    page.app()

x = st.sidebar.success(f"Sucessfully loaded {selection} ...")
time.sleep(0.2)
x.empty()
st.sidebar.info('© Digital-Lab')
