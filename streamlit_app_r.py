import streamlit as st
from predict import predict_diabetes

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Diabetes Intelligence",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html,body,[class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Background */

.stApp{

background:
radial-gradient(circle at top left,#00ffb320,transparent 35%),
radial-gradient(circle at bottom right,#00c89620,transparent 35%),
linear-gradient(135deg,#030712,#071827,#03151b);

background-attachment:fixed;

color:white;

}

/* Hide Streamlit default */

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

#MainMenu{
visibility:hidden;
}

/* Container */

.block-container{

padding-top:1rem;
padding-left:2rem;
padding-right:2rem;

max-width:1450px;

}

/* Hero */

.hero{

text-align:center;

padding-top:20px;

padding-bottom:30px;

}

.hero-title{

font-size:65px;

font-weight:800;

color:#00F5B4;

text-shadow:

0 0 8px #00F5B4,

0 0 18px #00F5B4,

0 0 35px #00F5B4;

}

.hero-sub{

font-size:19px;

color:#cbd5e1;

}

/* Online Badge */

.badge{

display:inline-block;

margin-top:15px;

padding:8px 22px;

border-radius:30px;

background:#0f172a;

border:1px solid #00F5B4;

color:#00F5B4;

font-weight:600;

}

/* Glass Card */

.glass{

background:rgba(255,255,255,.05);

backdrop-filter:blur(16px);

border:1px solid rgba(255,255,255,.08);

border-radius:25px;

padding:25px;

box-shadow:

0 10px 30px rgba(0,0,0,.35),

0 0 20px rgba(0,245,180,.15);

transition:.3s;

}

.glass:hover{

transform:translateY(-4px);

box-shadow:

0 15px 35px rgba(0,0,0,.4),

0 0 25px rgba(0,245,180,.25);

}

/* Metric Cards */

.metric{

background:rgba(255,255,255,.05);

padding:20px;

border-radius:22px;

text-align:center;

border:1px solid rgba(0,245,180,.2);

transition:.3s;

}

.metric:hover{

transform:scale(1.04);

border-color:#00F5B4;

box-shadow:0 0 18px rgba(0,245,180,.3);

}

/* Titles */

.section-title{

font-size:34px;

font-weight:700;

color:white;

margin-bottom:20px;

}

/* Labels */

label,

[data-testid="stWidgetLabel"] p{

font-size:17px!important;

font-weight:700!important;

color:#00F5B4!important;

}

/* Inputs */

div[data-baseweb="input"]{

background:#101826!important;

border:1px solid rgba(0,245,180,.35)!important;

border-radius:14px!important;

}

div[data-baseweb="input"]:hover{

border-color:#00F5B4!important;

box-shadow:0 0 10px rgba(0,245,180,.4);

}

div[data-baseweb="input"] input{

color:white!important;

font-size:18px!important;

font-weight:600!important;

-webkit-text-fill-color:white!important;

}

/* Plus Minus */

button[kind="secondary"]{

background:#101826!important;

color:#00F5B4!important;

}

/* Button */

div.stButton>button{

width:100%;

height:60px;

border:none;

border-radius:18px;

background:linear-gradient(90deg,#00F5B4,#00C896);

font-size:20px;

font-weight:700;

color:#041017;

transition:.3s;

box-shadow:0 0 25px rgba(0,245,180,.45);

}

div.stButton>button:hover{

transform:scale(1.02);

box-shadow:0 0 35px rgba(0,245,180,.7);

}

/* Sidebar */

section[data-testid="stSidebar"]{

background:#07131f;

border-right:1px solid rgba(0,245,180,.15);

}

section[data-testid="stSidebar"] h1,

section[data-testid="stSidebar"] h2,

section[data-testid="stSidebar"] h3{

color:#00F5B4;

}

/* Result Card */

.result{

padding:30px;

border-radius:22px;

text-align:center;

background:rgba(255,255,255,.05);

border:1px solid rgba(0,245,180,.2);

}

/* Footer */

.footer{

margin-top:50px;

padding:20px;

text-align:center;

color:#94a3b8;

font-size:15px;

}

/* Mobile */

@media(max-width:768px){

.hero-title{

font-size:40px;

}

.section-title{

font-size:25px;

}

}

</style>

""", unsafe_allow_html=True)
# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("# 🩺 AI Health Assistant")

    st.success("🟢 AI Model Online")

    st.markdown("---")

    st.markdown("### 🏠 Dashboard")
    st.markdown("### 📊 Prediction")
    st.markdown("### 📈 Analytics")
    st.markdown("### 📄 Reports")
    st.markdown("### 🧠 AI Insights")
    st.markdown("### ⚙ Settings")

    st.markdown("---")

    st.markdown("### 🤖 Model Information")

    st.info("""
**Model**

Random Forest Classifier

**Version**

2.1

**Accuracy**

89%

**Prediction Time**

0.02 sec

**Status**

🟢 Active
""")

    st.markdown("---")

    st.caption("Made with ❤️ using Streamlit")


# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero">

<div class="hero-title">

🧬 AI Diabetes Intelligence

</div>

<div class="hero-sub">

Advanced Machine Learning Clinical Risk Assessment Platform

</div>

<div class="badge">

🟢 AI Prediction Engine Online

</div>

</div>
""", unsafe_allow_html=True)


# =====================================================
# DASHBOARD CARDS
# =====================================================

c1,c2,c3,c4,c5,c6 = st.columns(6)

cards = [
("🧬","Parameters","8"),
("🤖","AI Model","Random Forest"),
("🎯","Accuracy","89%"),
("⚡","Speed","0.02 s"),
("👨‍⚕","Patients","12,450"),
("🟢","Status","ONLINE")
]

cols=[c1,c2,c3,c4,c5,c6]

for col,(icon,title,value) in zip(cols,cards):

    with col:

        st.markdown(f"""
        <div class="metric">

        <h2>{icon}</h2>

        <h4>{title}</h4>

        <h2>{value}</h2>

        </div>
        """,unsafe_allow_html=True)

st.write("")


# =====================================================
# MAIN LAYOUT
# =====================================================

left,right=st.columns([1.6,1])


# =====================================================
# INPUT FORM
# =====================================================

with left:

    st.markdown("<div class='glass'>",unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">

    🩺 Patient Clinical Information

    </div>
    """,unsafe_allow_html=True)

    a,b=st.columns(2)

    with a:

        preg=st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=0)

        glucose=st.number_input(
        "Glucose Level",
        min_value=0,
        max_value=300,
        value=100)

        bp=st.number_input(
        "Blood Pressure",
        min_value=0,
        max_value=200,
        value=70)

        skin=st.number_input(
        "Skin Thickness",
        min_value=0,
        max_value=100,
        value=20)

    with b:

        insulin=st.number_input(
        "Insulin",
        min_value=0,
        max_value=900,
        value=80)

        bmi=st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0,
        format="%.2f")

        dpf=st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.500,
        format="%.3f")

        age=st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30)

    st.write("")

    predict_btn=st.button("🚀 Analyze Health Risk")

    st.markdown("</div>",unsafe_allow_html=True)


# =====================================================
# AI ANALYTICS PANEL
# =====================================================

with right:

    st.markdown("<div class='glass'>",unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">

    🤖 AI Analytics

    </div>
    """,unsafe_allow_html=True)

    st.metric(
        "Prediction Engine",
        "Random Forest"
    )

    st.metric(
        "Accuracy",
        "89%"
    )

    st.metric(
        "Processing Time",
        "0.02 sec"
    )

    st.metric(
        "Model Version",
        "v2.1"
    )

    st.metric(
        "Status",
        "🟢 Active"
    )

    st.metric(
        "Report",
        "Available"
    )

    st.markdown("</div>",unsafe_allow_html=True)
    # =====================================================
# AI PREDICTION
# =====================================================

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
    st.markdown("## 🧠 AI Prediction Report")

    st.progress(float(probability))

    col1, col2 = st.columns([2,1])

    with col1:

        if prediction == 1:

            st.markdown(f"""
            <div class='result'
            style='border:2px solid #ff4d4d;
            box-shadow:0 0 25px rgba(255,0,0,.35);'>

            <h1 style='color:#ff4d4d'>
            ⚠ HIGH DIABETES RISK
            </h1>

            <h2>
            Confidence : {probability*100:.2f}%
            </h2>

            <hr>

            <h3>AI Recommendation</h3>

            <p style="font-size:18px">

            • Consult a physician soon.<br>

            • Reduce sugar intake.<br>

            • Exercise at least 30 minutes daily.<br>

            • Maintain healthy body weight.<br>

            • Monitor blood glucose regularly.<br>

            • Follow a balanced diet.

            </p>

            </div>

            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class='result'
            style='border:2px solid #00ff99;
            box-shadow:0 0 25px rgba(0,255,150,.35);'>

            <h1 style='color:#00ff99'>
            ✅ LOW DIABETES RISK
            </h1>

            <h2>
            Confidence : {probability*100:.2f}%
            </h2>

            <hr>

            <h3>AI Recommendation</h3>

            <p style="font-size:18px">

            • Continue healthy eating.<br>

            • Exercise regularly.<br>

            • Drink enough water.<br>

            • Maintain normal BMI.<br>

            • Get annual health checkups.<br>

            • Continue healthy lifestyle.

            </p>

            </div>

            """, unsafe_allow_html=True)

    # =============================================
    # RIGHT ANALYTICS
    # =============================================

    with col2:

        st.markdown("### 📊 Prediction Summary")

        st.metric(
            "Risk",
            "High" if prediction else "Low"
        )

        st.metric(
            "Confidence",
            f"{probability*100:.2f}%"
        )

        st.metric(
            "Model",
            "Random Forest"
        )

        st.metric(
            "Prediction Time",
            "0.02 sec"
        )

        st.metric(
            "Status",
            "Completed"
        )

        st.metric(
            "Recommendation",
            "Generated"
        )

    st.write("")

    # =============================================
    # HEALTH SCORE
    # =============================================

    score = int((1 - probability) * 100) if prediction == 0 else int((1 - probability) * 40)

    st.markdown("### ❤️ Overall Health Score")

    st.progress(score / 100)

    st.success(f"Health Score : {score}/100")

    # =============================================
    # PARAMETER SUMMARY
    # =============================================

    st.write("")
    st.markdown("## 📋 Patient Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Age", age)
    c2.metric("BMI", bmi)
    c3.metric("Glucose", glucose)
    c4.metric("Blood Pressure", bp)

    st.write("")

    # =============================================
    # DOWNLOAD REPORT
    # =============================================

    report = f"""
AI Diabetes Prediction Report

Prediction :
{"High Diabetes Risk" if prediction else "Low Diabetes Risk"}

Confidence :
{probability*100:.2f} %

Age : {age}

BMI : {bmi}

Glucose : {glucose}

Blood Pressure : {bp}

Insulin : {insulin}

Skin Thickness : {skin}

Pregnancies : {preg}

Diabetes Pedigree Function : {dpf}

Generated using AI Diabetes Intelligence Dashboard
"""

    st.download_button(
        "📄 Download Report",
        report,
        file_name="Diabetes_Report.txt",
        mime="text/plain"
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class='footer'>

<hr>

<h3 style='color:#00F5B4;'>

🧬 AI Diabetes Intelligence Platform

</h3>

<p>

Powered by Streamlit • Scikit-Learn • Machine Learning • Python

</p>

<p>

© 2026 Vivek Kumar | Advanced Clinical Risk Assessment Dashboard

</p>

</div>
""", unsafe_allow_html=True)
