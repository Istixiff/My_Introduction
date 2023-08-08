import streamlit as st
import requests
from streamlit_lottie import st_lottie
import logging

# Enable Streamlit's native debugger
st.experimental_set_query_params(debug=True)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Set custom page icon (favicon)
st.set_page_config(
    page_title="My Introduction",
    page_icon="icons/semi.png",  # Replace with the actual path to your icon
    layout="wide"
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/4490a729-248a-48df-897e-9f6b19627935/oDQNLZfAsV.json")
lottie_coding2 = load_lottieurl2("https://lottie.host/e9fe6ce2-66e5-46c9-b0fd-a936d844685c/ib0WotdAuY.json")

# Custom CSS to set background image
background_style = """
.stApp {
    background-image: url('https://mir-s3-cdn-cf.behance.net/project_modules/1400/0587f251249217.58e7079c0894c.gif');
    background-size: cover;
    background-repeat: no-repeat;
}
"""

st.write("<style>" + background_style + "</style>", unsafe_allow_html=True)

# Main Content
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Hello I'm Semi :wave:")
        st.subheader("About Me")
        st.write(" - I'm 16 in High School")
        st.write(" - I'm still new to coding")
        st.write(" - I just want to make money off of coding")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Add debugging logging statements
logging.debug("Lottie animation loaded successfully")

# Projects Section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("---")
        st.header("My Projects")
        st.write("##")
        st.write(" - I don't have any projects as of right now")
    with right_column:
        st_lottie(lottie_coding2, height=300, key="coding2")

# Connections Section
with st.container():
    st.write("---")
    st.header("Connections")

    # Button styles
    button_style = (
        "background-color: #010101; color: white; border: none; border-radius: 5px; "
        "width: 150px; height: 35px; display: flex; align-items: center; justify-content: center;"
    )

    discord_url = "https://discord.gg/YUJn9mKdyn"
    twitter_url = "https://twitter.com/Istixif"
    instagram_url = "https://instagram.com/alanrangel926?utm_source=qr&igshid=MzNlNGNkZWQ4Mg%3D%3D"
    youtube_url = "https://youtube.com/@semi6227"

    # Discord button
    button_html = f"""
    <a href="{discord_url}" target="_blank" style="{button_style}">
        My Discord Server
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)

    # Twitter button
    button_html = f"""
    <a href="{twitter_url}" target="_blank" style="{button_style}">
        My Twitter
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)

    # Instagram button
    button_html = f"""
    <a href="{instagram_url}" target="_blank" style="{button_style}">
        My Instagram
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)

    # YouTube button
    button_html = f"""
    <a href="{youtube_url}" target="_blank" style="{button_style}">
        My Youtube
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)

    # Add debugging logging statements
    logging.debug("Connections section rendered")

# Ways to Contact Me Section
with st.container():
    st.write("---")
    st.header("Ways to Contact Me")
    st.write("##")
    st.write(" - My Discord - Semi.s")
    st.write(" - My Phone Number - [719-309-8271](tel:7193098271)")
    st.write(" - My Email")

    # Contact form
    contact_form = """
        <form action="https://formsubmit.co/istixifpdr@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

    # Add debugging logging statements
    logging.debug("Ways to Contact Me section rendered")
