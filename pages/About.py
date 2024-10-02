import streamlit as st
from PIL import Image
from helper_functions import load_css

st.set_page_config(layout='wide')
load_css()
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

IMAGE_SIZE = (128, 128)

st.header("About Travel.ai")
st.subheader("")
st.write("At Travel.ai, we revolutionized travel planning to alleviate the common headaches encountered during trip scheduling. \
         By integrating advanced AI technology, we streamline the entire process, providing personalized itineraries, optimizing travel routes, and enhancing the overall user experience. \
         Say goodbye to the stress of planning and embrace seamless travel with Travel.ai.")


st.header("About the developers")
st.write("We're dudes who love building stuff. Feel to reach out to us through our socials and share your feedback")

col1, col2 = st.columns([2,1])

fa_li = """
<i class="fab fa-linkedin"></i>
"""
fa_em = """
<i class="far fa-envelope"></i>
"""


with col1:
    hari = Image.open('assets/images/hari - Hariharan Ayappane.jpg').resize(IMAGE_SIZE)
    st.header('Hari')
    st.write('"Cracked guy who likes to F around and find out"')
    st.write("\n")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        st.image(hari)

    linkedin_url='https://www.linkedin.com/in/hariharan-ayappane'
    twitter_url='https://x.com/HariAyapps'
    github_url='https://github.com/haran2001'
    st.markdown(f"""
    <div style="display: flex; justify-content: center; gap: 10px;">
        <a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="40" height="40">
        </a>
        <a href="{github_url}" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" width="40" height="40">
        </a>
        <a href="{twitter_url}" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg" alt="Twitter" width="40" height="40">
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    rishab = Image.open('assets/images/rishab.png').resize(IMAGE_SIZE)
    st.header('Rishab')
    st.write('"Another cracked guy"')
    st.write("\n")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        st.image(rishab)

    linkedin_url='https://www.linkedin.com/in/hariharan-ayappane'
    github_url='https://github.com/haran2001'
    st.markdown(f"""
    <div style="display: flex; justify-content:center; gap: 10px;">
        <a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="40" height="40">
        </a>
        <a href="{github_url}" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" width="40" height="40">
        </a>
    </div>
    """, unsafe_allow_html=True)

st.write("\n")