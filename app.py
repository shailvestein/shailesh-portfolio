
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page Configuration
st.set_page_config(page_title="AI/DL Portfolio", page_icon="🤖", layout="wide")

# ---- CUSTOM CSS FOR ANIMATIONS & STYLING ----
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Gradient Background Effect */
    .main {
        background: radial-gradient(circle at top left, #0e1117, #1a1c24);
    }

    /* Glassmorphism Card Effect */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease, border 0.3s ease;
        margin-bottom: 20px;
    }

    .project-card:hover {
        transform: translateY(-10px);
        border: 1px solid #00d4ff;
        box-shadow: 0px 10px 30px rgba(0, 212, 255, 0.2);
    }

    /* Neural Link Animation */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00d4ff , #0055ff);
    }

    /* Title Styling */
    .glitch-text {
        color: white;
        font-size: 50px;
        font-weight: 700;
        text-shadow: 2px 2px #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# ---- ASSETS LOADING ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_g3p3bh9p.json") # AI Brain
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_w51pcehl.json")

# ---- HEADER SECTION ----
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<h1 class="glitch-text">Hello, I\'m a Deep Learning Engineer 🚀</h1>', unsafe_allow_html=True)
        st.write("Building the future with Neural Networks, Computer Vision, and Generative AI.")
        st.button("Download Resume")
    with col2:
        st_lottie(lottie_ai, height=300, key="coding")

st.write("---")

# ---- PROJECTS SECTION ----
st.header("🔬 Featured Research & Projects")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div class="project-card">
            <h3>🖼️ Retinexformer Enhancement</h3>
            <p>Low-light image enhancement using transformer-based architectures. Achieved state-of-the-art results in denoising and illumination correction.</p>
            <small>Tech: PyTorch, Restormer, CUDA</small>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="project-card">
            <h3>🏥 Medical Report Analyzer</h3>
            <p>An end-to-end pipeline to predict personalized diet plans by analyzing scanned medical reports using OCR and NLP.</p>
            <small>Tech: Tesseract, HuggingFace, Streamlit</small>
        </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
        <div class="project-card">
            <h3>🏏 Cricket Speed Tracker</h3>
            <p>Real-time bowling speed estimation using YOLOv8 and multi-object tracking (MOT) on mobile-recorded footage.</p>
            <small>Tech: YOLOv11, OpenCV, Computer Vision</small>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="project-card">
            <h3>🧠 Ensemble Vision Pipeline</h3>
            <p>A modular training framework that combines Retinexformer, ESDNet, and CIDNet for NTIRE 2025 challenges.</p>
            <small>Tech: PyTorch, Modular Coding, GANs</small>
        </div>
    """, unsafe_allow_html=True)

# ---- SKILLS SECTION (Animated Bars) ----
st.write("---")
st.header("⚡ Core Tech Stack")
col_s1, col_s2 = st.columns(2)

with col_s1:
    st.write("PyTorch & Deep Learning")
    st.progress(95)
    st.write("Computer Vision (OpenCV/YOLO)")
    st.progress(90)

with col_s2:
    st.write("Python Development")
    st.progress(85)
    st.write("Model Deployment (Docker/Streamlit)")
    st.progress(80)

# ---- FOOTER ----
st.write("---")
st.markdown("<center>Made with ❤️ and Neural Networks | 2026</center>", unsafe_allow_html=True)
