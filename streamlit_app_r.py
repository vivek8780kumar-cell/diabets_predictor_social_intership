import streamlit as st
from predict import predict_diabetes

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="AI Diabetes Dashboard",
    page_icon="🩺",
    layout="wide"
)

# ================= CSS ================= #

st.markdown("""
<style>

.stApp{
    background:
    radial-gradient(circle at top left,
    rgba(0,255,180,0.12),
    transparent 35%),

    radial-gradient(circle at bottom right,
    rgba(0,255,180,0.12),
    transparent 35%),

    #020814;

    color:white;
}

/* Hide Streamlit header */
header{
    visibility:hidden;
}

.block-container{
    padding-top:1rem;
    max-width:1400px;
}

/* Hero */

.hero{
    text-align:center;
    padding:20px;
}

.hero-title{
    font-size:60px;
    font-weight:800;
    color:#00f5b4;
    text-shadow:0px 0px 25px #00f5b4;
}

.hero-sub{
    font-size:20px;
    color:#b0bec5;
}

/* Glass card */

.glass{
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,0.08);

    border-radius:25px;
    padding:30px;

    box-shadow:
    0px 0px 35px rgba(0,255,180,0.12);
}

/* Metrics */

.metric{
    background:rgba(255,255,255,0.04);

    border:1px solid rgba(0,255,180,0.2);

    border-radius:20px;

    padding:20px;

    text-align:center;
}

/* Labels */

label,
[data-testid="stWidgetLabel"] p{
    color:#00f5b4 !important;
    font-size:18px !important;
    font-weight:700 !important;
}

/* Number Input */

div[data-baseweb="input"]{
    background:#111827 !important;
    border:1px solid rgba(0,255,180,0.35) !important;
    border-radius:16px !important;
}

/* Input text */

div[data-baseweb="input"] input{
    color:white !important;
    font-size:18px !important;
    font-weight:600 !important;
    -webkit-text-fill-color:white !important;
}

/* Plus Minus buttons */

button[kind="secondary"]{
    background:#111827 !important;
    color:#00f5b4 !important;
}

/* Hover */

div[data-baseweb="input"]:hover{
    border:1px solid #00f5b4 !important;
    box-shadow:0px 0px 15px rgba(0,255,180,0.45);
}

/* Analyze Button */

/* Button */

div.stButton > button{

    width:100%;
    height:60px;

    border:none;
    border-radius:18px;

    background:
    linear-gradient(
    90deg,
    #00f5b4,
    #00c896
    );

    color:black;
    font-size:20px;
    font-weight:bold;

    box-shadow:
    0px 0px 25px rgba(0,255,180,0.5);
}

div.stButton > button:hover{

    transform:scale(1.02);

    box-shadow:
    0px 0px 40px rgba(0,255,180,0.8);
}

/* Result */

/* Result Card */

.result-card{
    padding:35px;
    border-radius:25px;
    text-align:center;
    background:rgba(255,255,255,0.05);
}

</style>
""", unsafe_allow_html=True)

# ================= HERO ================= #

st.markdown("""
<div class="hero">

<div class="hero-title">
AI Diabetes Dashboard
</div>

<div class="hero-sub">
Advanced Clinical Risk Assessment System
</div>

</div>
""", unsafe_allow_html=True)

# ================= METRICS ================= #

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class='metric'>
    <h4>Parameters</h4>
    <h2>8</h2>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class='metric'>
    <h4>AI Model</h4>
    <h2>ML</h2>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class='metric'>
    <h4>Accuracy</h4>
    <h2>89%</h2>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class='metric'>
    <h4>Status</h4>
    <h2>LIVE</h2>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ================= MAIN SECTION ================= #

left, right = st.columns([1.5,1])

with left:

    st.markdown("<div class='glass'>",
                unsafe_allow_html=True)

    st.markdown("""
    <h2 style='color:white'>
    🩺 Patient Clinical Information
    </h2>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        preg = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=0,
            step=1
        )

        glucose = st.number_input(
            "Glucose Level",
            min_value=0,
            max_value=300,
            value=100,
            step=1
        )

        bp = st.number_input(
            "Blood Pressure",
            min_value=0,
            max_value=200,
            value=70,
            step=1
        )

        skin = st.number_input(
            "Skin Thickness",
            min_value=0,
            max_value=100,
            value=20,
            step=1
        )

    with c2:

        insulin = st.number_input(
            "Insulin",
            min_value=0,
            max_value=900,
            value=80,
            step=1
        )

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=70.0,
            value=25.0,
            step=0.1,
            format="%.2f"
        )

        dpf = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.0,
            max_value=3.0,
            value=0.500,
            step=0.001,
            format="%.3f"
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=30,
            step=1
        )

    predict_btn = st.button(
        "🚀 Analyze Health Risk"
    )

    st.markdown("</div>",
                unsafe_allow_html=True)

# ================= RIGHT PANEL ================= #

with right:

    st.markdown("""
    <div class='glass'>

    <h2 style='color:#00f5b4'>
    🤖 AI Analytics
    </h2>

    <br>

    ✔ Machine Learning Prediction<br><br>

    ✔ Diabetes Risk Analysis<br><br>

    ✔ Confidence Score<br><br>

    ✔ Clinical Decision Support<br><br>

    ✔ Real-time Dashboard

    </div>
    """, unsafe_allow_html=True)

# ================= PREDICTION ================= #

if predict_btn:

    prediction, probability = predict_diabetes([
        preg,
        glucose,
        bp,
        skin,
        insulin,
        bmi,
        dpf,
        age
    ])

    st.subheader("🧠 Prediction Result")

    st.progress(float(probability))

    if prediction == 1:

        st.markdown(f"""
        <div class='result-card'
        style='border:2px solid #ff4d4d;'>

        <h1 style='color:#ff4d4d'>
        ⚠ High Diabetes Risk
        </h1>

        <h2>
        Confidence:
        {probability*100:.2f}%
        </h2>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class='result-card'
        style='border:2px solid #00ff99;'>

        <h1 style='color:#00ff99'>
        ✅ Low Diabetes Risk
        </h1>

        <h2>
        Confidence:
        {probability*100:.2f}%
        </h2>

        </div>
        """, unsafe_allow_html=True)

# ================= SIDEBAR ================= #

st.sidebar.title("🤖 AI Health Assistant")

st.sidebar.info("""
Advanced AI-powered diabetes prediction dashboard.

Features:

• Diabetes Risk Prediction  
• Clinical Analytics  
• Confidence Score  
• AI Decision Support  
• Real-time Dashboard
""")

st.sidebar.success("Model Status : Active ✅")
