import streamlit as st
from predict import predict_diabetes

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
    rgba(0,255,180,0.15), transparent 35%),
    radial-gradient(circle at bottom right,
    rgba(0,255,180,0.12), transparent 35%),
    #020814;
    color:white;
}

header{
    visibility:hidden;
}

.block-container{
    padding-top:1rem;
}

/* Hero */

.hero{
    text-align:center;
    padding:20px;
}

.hero-title{
    font-size:65px;
    font-weight:800;
    color:#00f5b4;
    text-shadow:0px 0px 30px #00f5b4;
}

.hero-sub{
    color:#b0bec5;
    font-size:20px;
}

/* Cards */

.glass{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(18px);

    border-radius:25px;
    padding:30px;

    box-shadow:
    0px 0px 40px rgba(0,255,180,0.12);
}

/* Metric cards */

.metric{
    background:rgba(255,255,255,0.04);
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(0,255,180,0.2);
}

/* Labels */

label,
[data-testid="stWidgetLabel"] p{
    color:#00f5b4 !important;
    font-size:18px !important;
    font-weight:700 !important;
}

/* Slider value */

.stSlider div{
    color:white !important;
}

/* Progress */

.stProgress > div > div{
    background:#00f5b4;
}

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

.result{
    padding:35px;
    border-radius:25px;
    text-align:center;
    background:rgba(255,255,255,0.05);
}

</style>
""", unsafe_allow_html=True)

# ================= HERO ================= #

st.markdown("""
<div class='hero'>
<div class='hero-title'>
AI Diabetes Dashboard
</div>

<div class='hero-sub'>
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

# ================= MAIN ================= #

left, right = st.columns([1.5,1])

with left:

    st.markdown(
    "<div class='glass'>",
    unsafe_allow_html=True)

    st.subheader("🩺 Patient Clinical Information")

    c1, c2 = st.columns(2)

    with c1:

        preg = st.slider(
            "Pregnancies",
            0,20,0
        )

        glucose = st.slider(
            "Glucose Level",
            0,300,100
        )

        bp = st.slider(
            "Blood Pressure",
            0,200,70
        )

        skin = st.slider(
            "Skin Thickness",
            0,100,20
        )

    with c2:

        insulin = st.slider(
            "Insulin",
            0,900,80
        )

        bmi = st.slider(
            "BMI",
            0.0,70.0,25.0
        )

        dpf = st.slider(
            "Diabetes Pedigree Function",
            0.0,3.0,0.5
        )

        age = st.slider(
            "Age",
            1,120,30
        )

    predict_btn = st.button(
        "🚀 Analyze Health Risk"
    )

    st.markdown("</div>",
    unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class='glass'>

    <h2 style='color:#00f5b4'>
    🤖 AI Analytics
    </h2>

    <br>

    ✔ Machine Learning Prediction<br><br>

    ✔ Diabetes Risk Assessment<br><br>

    ✔ Confidence Scoring<br><br>

    ✔ Health Analytics Dashboard<br><br>

    ✔ Clinical Decision Support

    </div>
    """,
    unsafe_allow_html=True)

# ================= RESULT ================= #

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

    st.write("")
    st.subheader("🧠 Prediction Result")

    st.progress(float(probability))

    if prediction == 1:

        st.markdown(f"""
        <div class='result'
        style='border:2px solid #ff4d4d;'>

        <h1 style='color:#ff4d4d'>
        ⚠ High Diabetes Risk
        </h1>

        <h2>
        Confidence:
        {probability*100:.2f}%
        </h2>

        </div>
        """,
        unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class='result'
        style='border:2px solid #00ff99;'>

        <h1 style='color:#00ff99'>
        ✅ Low Diabetes Risk
        </h1>

        <h2>
        Confidence:
        {probability*100:.2f}%
        </h2>

        </div>
        """,
        unsafe_allow_html=True)

# ================= SIDEBAR ================= #

st.sidebar.title("🤖 AI Health Assistant")

st.sidebar.info("""
Advanced AI-powered health analytics dashboard.

Features:

• Diabetes Prediction  
• Risk Analytics  
• Confidence Score  
• AI Decision Support  
• Clinical Dashboard
""")

st.sidebar.success("Model Status : Active ✅")
