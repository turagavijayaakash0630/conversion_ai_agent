import streamlit as st
from crawler import crawl_website, generate_website_summary, simulate_users
from ai_agent import analyze_website, improve_website

# Page config
st.set_page_config(
    page_title="AI Website Conversion rate Optimizer",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>


body {
    background: radial-gradient(circle at top, #020617, #000000);
    background-size: 200% 200%;
    animation: bgMove 15s ease infinite;
    color: e5f0ff;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Main container */
.main {
    padding: 20px;
}

/* Glass AI Panels */
.card {
    background: rgba(0, 255, 255, 0.05);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 25px;
    border: 1px solid rgba(0, 255, 255, 0.25);
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.25);
    transition: all 0.3s ease-in-out;
    position: relative;
}

/* Glowing edges on hover */
.card:hover {
    transform: scale(1.01);
    box-shadow: 0 0 50px rgba(0, 255, 255, 0.6);
}


.ai-title {
    font-size: 50px;
    font-weight: 900;
    text-align: center;
    letter-spacing: 2px;
    color: black;
    text-shadow: none;
    margin-bottom: 10px;
}


/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #ff57ff;
    margin-bottom: 35px;
    letter-spacing: 1px;
}

/* Highlight */
.highlight {
    color: #00ff88;
    font-weight: bold;
}

/* Good / Bad values */
.good {
    color: #00ff88;
    font-weight: bold;
}
.bad {
    color: #ff4d4d;
    font-weight: bold;
}

/* Button - AI Neon */
.stButton>button {
    background: linear-gradient(90deg, #00ffff, #00ff88);
    color: black;
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 25px;
    border: none;
    box-shadow: 0 0 18px rgba(0, 255, 255, 0.7);
    transition: all 0.3s ease-in-out;
    letter-spacing: 1px;
}

.stButton>button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 30px rgba(0, 255, 255, 1);
}

/* Input box futuristic */
input, textarea {
    background: rgba(0, 255, 255, 0.08) !important;
    color: black !important;        /* TEXT COLOR */
    caret-color: #00ffff !important; /* CURSOR COLOR */
    border-radius: 10px !important;
    border: 1px solid rgba(0, 255, 255, 0.6) !important;
    font-weight: 600 !important;
}


/* Section headers */
h1, h2, h3 {
    color: #00ffff;
    text-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
}

</style>
""", unsafe_allow_html=True)

# Header
# Header
st.markdown("<div class='ai-title'>🤖 WEBSITE CONVERSION RATE IMPROVER AGENT</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Autonomous Intelligence for Website Optimization</div>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>👋 Hi</h3>
    <p>
    I am your <b>website conversion rate improver agent</b>. My mission is to scan any website, 
    detect weaknesses in user behavior, rebuild the interface using advanced AI logic, 
    and <span class="highlight">optimize conversion performance</span>.
    </p>
    <p>
    📡 Input a website URL below. I will analyze, upgrade, and demonstrate improvement.
    </p>
</div>
""", unsafe_allow_html=True)



# Input Section
st.markdown("## 🌐 Website Input")
url = st.text_input("Enter any website URL", placeholder="https://example.com")

if st.button("✨ Analyze & Optimize"):
    with st.spinner("Crawling website and activating AI agent..."):
        data = crawl_website(url)

    if data:
        st.success("Website successfully analyzed by AI!")

        # Original Website Data
        st.markdown("## 🔴 Original Website (Version A)")
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.json(data)
            st.markdown("</div>", unsafe_allow_html=True)

        # AI Input Summary
        summary = generate_website_summary(data)
        st.markdown("## 🧠 AI Understanding of the Website")
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.write(summary)
            st.markdown("</div>", unsafe_allow_html=True)

        # AI Analysis
        with st.spinner("AI analyzing conversion problems..."):
            ai_issues = analyze_website(summary)

        st.markdown("## ⚠️ Conversion Issues Detected by AI")
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.write(ai_issues)
            st.markdown("</div>", unsafe_allow_html=True)

        # AI Improvement
        with st.spinner("AI generating improved website..."):
            improved_site = improve_website(summary)

        st.markdown("## ✨ AI-Improved Website (Version B)")
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.write(improved_site)
            st.markdown("</div>", unsafe_allow_html=True)

        # Conversion Simulation
        st.markdown("## 📊 AI Conversion Performance")

        users = 1000
        original_quality = 0.02
        improved_quality = 0.05

        orig_conv, orig_rate = simulate_users(original_quality, users)
        imp_conv, imp_rate = simulate_users(improved_quality, users)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 🔴 Original Website")
            st.write(f"👥 Users: {users}")
            st.write(f"✅ Converted: {orig_conv}")
            st.markdown(f"📉 Conversion Rate: <span class='bad'>{orig_rate:.2f}%</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 🟢 AI-Improved Website")
            st.write(f"👥 Users: {users}")
            st.write(f"✅ Converted: {imp_conv}")
            st.markdown(f"📈 Conversion Rate: <span class='good'>{imp_rate:.2f}%</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        improvement = imp_rate - orig_rate
        with col3:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 🚀 AI Impact")
            st.markdown(f"🔥 Conversion Boost: <span class='highlight'>+{improvement:.2f}%</span>", unsafe_allow_html=True)
            st.markdown("💡 AI successfully optimized the website for better user action.")
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.error("❌ Could not analyze the website. Try a different URL.")
