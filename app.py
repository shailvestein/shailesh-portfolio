import streamlit as st
from streamlit_lottie import st_lottie
import requests

# 1. Page Configuration
st.set_page_config(page_title="DL Portfolio | Shailesh", page_icon="🧠", layout="wide")

# 2. Function to load Lottie Assets with Error Handling
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# Load Animations (New Stable Links)
lottie_ai = load_lottieurl("https://lottie.host/80860538-232a-4467-8739-1667d730a867/G6YJ4x1v4y.json")
lottie_tech = load_lottieurl("https://lottie.host/578f108b-663f-4e56-8349-f538e6e58983/S7Y8S6t4QZ.json")

# 3. Custom CSS (Deep Learning & Glassmorphism Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }

    /* Modern Card Style */
    .project-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 20px;
    }

    .project-card:hover {
        transform: translateY(-8px) scale(1.02);
        border: 1px solid #00d4ff;
        box-shadow: 0px 15px 35px rgba(0, 212, 255, 0.15);
        background: rgba(255, 255, 255, 0.07);
    }

    .glitch-text {
        background: -webkit-linear-gradient(#eee, #333);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 55px;
        font-weight: 900;
        line-height: 1.2;
    }

    .tech-tag {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 50px;
        background: rgba(0, 212, 255, 0.1);
        color: #00d4ff;
        font-size: 12px;
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER SECTION
with st.container():
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown('<p style="color:#00d4ff; font-weight:bold;">DEEP LEARNING ENGINEER</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="glitch-text">Designing the Neural <br>Future.</h1>', unsafe_allow_html=True)
        st.write("Specializing in Image Restoration, Computer Vision, and Generative Models.")
        
        # Action Buttons
        btn_col1, btn_col2 = st.columns([1, 2])
        with btn_col1:
            st.button("View GitHub")
        with btn_col2:
            st.button("Download CV")

    with col2:
        if lottie_ai:
            st_lottie(lottie_ai, height=350, key="ai_brain")
        else:
            st.image("https://via.placeholder.com/350x350.png?text=AI+Core+Active", caption="Neural Engine")

st.markdown("<br><br>", unsafe_allow_html=True)

# 5. PROJECTS SECTION
st.header("⚡ Featured Intelligence")
st.write("---")

# Row 1
c1, c2 = st.columns(2)
with c1:
    st.markdown("""
        <div class="project-card">
            <h3>🖼️ Retinexformer Ensembles</h3>
            <p>Developing paper-level implementations for NTIRE 2025. Combining ESDNet and CIDNet for superior image restoration.</p>
            <span class="tech-tag">PyTorch</span><span class="tech-tag">Transformers</span><span class="tech-tag">NTIRE</span>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="project-card">
            <h3>🏏 Cricket Speed AI</h3>
            <p>Mobile-based bowling speed estimation using YOLOv11 and custom tracking logic for tennis ball detection.</p>
            <span class="tech-tag">YOLOv11</span><span class="tech-tag">OpenCV</span><span class="tech-tag">Android</span>
        </div>
    """, unsafe_allow_html=True)

# Row 2
c3, c4 = st.columns(2)
with c3:
    st.markdown("""
        <div class="project-card">
            <h3>🏥 Medical Diet Predictor</h3>
            <p>Predicting personalized diet charts from scanned medical reports using OCR and fine-tuned NLP models.</p>
            <span class="tech-tag">OCR</span><span class="tech-tag">HuggingFace</span><span class="tech-tag">Medical AI</span>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
        <div class="project-card">
            <h3>🎓 MCA Final Project</h3>
            <p>Advanced Computer Vision research project for IGNOU MCAOL, focusing on scalable deep learning architectures.</p>
            <span class="tech-tag">Academic</span><span class="tech-tag">Research</span><span class="tech-tag">Modular Coding</span>
        </div>
    """, unsafe_allow_html=True)

# 6. SKILLS SECTION
st.markdown("<br><br>", unsafe_allow_html=True)
st.header("🛠️ Tech Stack")

col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.write("**Architecture**")
    st.info("PyTorch, CNNs, Transformers")
with col_s2:
    st.write("**Vision Tools**")
    st.success("OpenCV, YOLOv11, Tesseract")
with col_s3:
    st.write("**Languages**")
    st.warning("Python, SQL, Modular Programming")

# 7. FOOTER
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <hr style="border:0.5px solid rgba(255,255,255,0.1)">
    <center style="opacity:0.6; font-size:14px;">
        Building Scalable AI Solutions | Powered by Streamlit & PyTorch | 2026
    </center>
""", unsafe_allow_html=True)
