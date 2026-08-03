"""
styles.py
---------
Centralized CSS for CareerCompass AI.
Provides a clean, modern blue theme while ensuring consistent rendering
across local development and Streamlit Community Cloud.
"""

import streamlit as st

CUSTOM_CSS = """
<style>

/* =========================================================
   Global Palette
========================================================= */
html, body {
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
}

/* App Background */
.stApp {
    background: linear-gradient(180deg, #F4F9FF 0%, #EAF2FB 100%);
    color: #0B1F3A;
}

/* Hide Streamlit UI */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* =========================================================
   Global Text
========================================================= */

h1, h2, h3 {
    color: #0B1F3A !important;
}

/* Paragraphs and markdown */
p,
li {
    color: #0B1F3A;
}

/* =========================================================
   Widget Labels (IMPORTANT)
========================================================= */

[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label,
.stRadio label,
.stSelectbox label,
.stSlider label,
.stTextInput label {
    color: #0B1F3A !important;
}

/* Radio button option text */
div[role="radiogroup"] label p {
    color: #0B1F3A !important;
}

/* Selectbox selected value */
div[data-baseweb="select"] * {
    color: #0B1F3A !important;
}

/* =========================================================
   Hero Banner
========================================================= */

.hero-banner {
    background: linear-gradient(
        135deg,
        #0B1F3A 0%,
        #1E5AA8 60%,
        #2E86DE 100%
    );

    padding: 2.5rem 2rem;
    border-radius: 18px;
    margin-bottom: 1.5rem;

    color: white;

    box-shadow: 0 10px 30px rgba(11,31,58,.25);
}

.hero-banner h1 {
    color: white !important;
    margin-bottom: .4rem;
}

.hero-banner p {
    color: #D6E8FA !important;
    margin: 0;
    font-size: 1.05rem;
}

/* =========================================================
   Cards
========================================================= */

.info-card {

    background: white;

    border: 1px solid #D6E8FA;

    border-radius: 14px;

    padding: 1.4rem 1.6rem;

    margin-bottom: 1rem;

    box-shadow: 0 4px 14px rgba(30,90,168,.08);

}

.career-card {

    background: white;

    border-left: 6px solid #2E86DE;

    border-radius: 14px;

    padding: 1.5rem 1.8rem;

    margin-bottom: 1.4rem;

    box-shadow: 0 6px 18px rgba(11,31,58,.10);

}

.career-card h3 {

    color: #0B1F3A !important;

    margin-top: 0;

}

.career-rank-badge {

    display: inline-block;

    background: #1E5AA8;

    color: white;

    font-weight: 600;

    font-size: .85rem;

    border-radius: 999px;

    padding: .15rem .7rem;

    margin-right: .6rem;

}

.compat-percentage {

    font-size: 1.6rem;

    font-weight: bold;

    color: #2E86DE;

}

.skill-chip {

    display: inline-block;

    background: #EAF2FB;

    color: #0B1F3A;

    border: 1px solid #D6E8FA;

    border-radius: 999px;

    padding: .25rem .75rem;

    margin: .2rem .3rem .2rem 0;

    font-size: .85rem;

}

/* =========================================================
   Buttons
========================================================= */

div.stButton > button {

    background: linear-gradient(135deg,#1E5AA8,#2E86DE);

    color: white;

    border: none;

    border-radius: 10px;

    font-weight: 600;

    padding: .6rem 1.4rem;

}

div.stButton > button:hover {

    color: white;

    transform: translateY(-1px);

    box-shadow: 0 6px 16px rgba(30,90,168,.35);

}

/* =========================================================
   Sidebar
========================================================= */

section[data-testid="stSidebar"] {

    background: #0B1F3A;

}

section[data-testid="stSidebar"] * {

    color: #EAF2FB !important;

}

/* =========================================================
   Progress Bar
========================================================= */

div[data-testid="stProgress"] > div > div {

    background-color: #2E86DE;

}

</style>
"""


def inject_custom_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)