import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Introduction", page_icon=":tada:", layout="wide")

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

lottie_coding = load_lottieurl("https://lottie.host/4490a729-248a-48df-897e-9f6b19627935/oDQNLZfAsV.json")
lottie_coding2 = load_lottieurl2("https://lottie.host/e9fe6ce2-66e5-46c9-b0fd-a936d844685c/ib0WotdAuY.json")

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

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("---")
        st.header("My Projects")
        st.write("##")
        st.write(" - I don't have any projects as of right now.")
    with right_column:
        st_lottie(lottie_coding2, height=300, key="coding2")

with st.container():
    st.write("---")
    st.header("Connections")
    st.write(" - [My Discord Server](https://discord.gg/YUJn9mKdyn)")
    st.write(" - [My Instagram](https://instagram.com/alanrangel926?utm_source=qr&igshid=MzNlNGNkZWQ4Mg%3D%3D)")
    st.write(" - [My Twitter](https://twitter.com/Istixif)")
    st.write(" - [My Youtube](https://youtube.com/@semi6227)")
    st.write(" - [My Github](https://github.com/Istixiff)")
    
with st.container():
    st.write("---")
    st.header("Ways to Contact Me")
    st.write("##")
    st.write(" - My Discord - Semi.s")
    st.write(" - My Phone Number - [719-309-8271](tel:7193098271)")
    st.write(" - My Email - istixifpdr@gmail.com")
    
