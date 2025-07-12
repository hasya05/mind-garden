import streamlit as st
import json
import random

# Load content
with open("content.json", "r") as f:
    content = json.load(f)

st.set_page_config(page_title="Mind Garden 🌸", layout="centered")

# Custom CSS for garden theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat&family=Quicksand:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
        background: linear-gradient(to top, #f8f3e7, #e0f7fa);
        color: #2d3436;
    }

    body::before {
        content: "";
        background: url("assets/background.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        opacity: 0.15;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }

    .main-title {
        font-size: 50px;
        font-family: 'Caveat', cursive;
        text-align: center;
        color: #6ab04c;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
        color: #218c74;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.6);
        border-left: 6px solid #81ecec;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        backdrop-filter: blur(5px);
    }

    .footer {
        text-align: center;
        font-size: 14px;
        margin-top: 40px;
        color: #44bd32;
    }

    a {
        color: #0984e3;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }
            
            @keyframes float {
    0% { transform: translateY(0px);}
    50% { transform: translateY(-10px);}
    100% { transform: translateY(0px);}
}

.floating-flower {
    animation: float 3s ease-in-out infinite;
}

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Mind Garden 🌸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Nourish your thoughts in bloom.</div>', unsafe_allow_html=True)

# Mood selection
moods = list(content.keys())

col1, col2 = st.columns([3, 1])
with col1:
    selected_mood = st.selectbox("🌼 What's your mood today?", ["Choose..."] + moods)

with col2:
    if st.button("🎲 Surprise Me!"):
        selected_mood = random.choice(moods)
        st.success(f"Surprise! You're now feeling **{selected_mood}** 🌟")

# Show content
if selected_mood and selected_mood != "Choose...":
    mood_data = content[selected_mood]

    st.markdown(f"<h3>🌺 Comfort for when you're feeling {selected_mood}:</h3>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("💬 Quote")
        st.write(f"_{mood_data['quote']}_")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("🎧 Podcast")
        st.write(f"**{mood_data['podcast']['title']}**")
        st.markdown(f"[Listen here]({mood_data['podcast']['link']})")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📺 Video")
        st.write(f"**{mood_data['video']['title']}**")
        st.markdown(f"[Watch here]({mood_data['video']['link']})")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📝 Article")
        st.write(f"**{mood_data['article']['title']}**")
        st.markdown(f"[Read here]({mood_data['article']['link']})")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">🌷 Made with love by Hasya · You deserve peace 🌷</div>', unsafe_allow_html=True)
st.markdown("""
    <style>
    @media (max-width: 768px) {
        .css-18e3th9 {
            padding: 1rem;
        }
        h1, h2, h3 {
            font-size: 1.2rem;
        }
        .stSelectbox label, .stButton {
            font-size: 0.9rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <img src="assets\flower1.pngg-flower" width="50">
""", unsafe_allow_html=True)

if st.checkbox("Save this for later"):
    st.success("Saved! (Feature under development)")


