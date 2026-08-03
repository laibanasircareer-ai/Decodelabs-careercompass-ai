"""
app.py
------
CareerCompass AI — a rule-based career recommendation system.

Main Streamlit entry point. Handles page routing (Home -> Assessment ->
Results) via st.session_state, and renders each page using the helper
modules: questionnaire.py, recommendation.py, careers_data.py, styles.py.
"""

import streamlit as st

from styles import inject_custom_css
from questionnaire import render_questionnaire, QUESTIONS
from recommendation import get_top_recommendations, build_explanation

# ---------------------------------------------------------------------------
# Page configuration (must be the first Streamlit call)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="CareerCompass AI",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_custom_css()

# ---------------------------------------------------------------------------
# Session state initialization
# ---------------------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"          # home | assessment | results
if "user_scores" not in st.session_state:
    st.session_state.user_scores = None      # dict of attribute -> score
if "user_name" not in st.session_state:
    st.session_state.user_name = ""


def go_to(page_name: str):
    """Simple page-router helper."""
    st.session_state.page = page_name
    st.rerun()


# ---------------------------------------------------------------------------
# Sidebar (visible on every page)
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🧭 CareerCompass AI")
    st.markdown("A rule-based technology career advisor.")
    st.markdown("---")
    st.markdown("**How it works**")
    st.markdown(
        "1. Answer 12 quick questions\n"
        "2. We score you against 8 tech careers\n"
        "3. Get your top 3 personalized matches"
    )
    st.markdown("---")
    if st.session_state.page != "home":
        if st.button("🔄 Start Over", use_container_width=True):
            st.session_state.page = "home"
            st.session_state.user_scores = None
            st.rerun()


# ---------------------------------------------------------------------------
# PAGE: HOME
# ---------------------------------------------------------------------------
def render_home():
    st.markdown(
        """
        <div class="hero-banner">
            <h1>🧭 CareerCompass AI</h1>
            <p>Discover the technology career that truly fits your strengths,
            interests, and working style — powered by transparent,
            rule-based logic (no black-box AI models involved).</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
            <h3>What you'll get</h3>
            <p>A short 12-question assessment covering programming, math,
            creativity, communication, AI &amp; cybersecurity interest,
            hardware vs. software preference, teamwork, leadership, and
            work style. Your answers are matched against weighted profiles
            for 8 in-demand technology careers, and you'll receive your
            <b>top 3 recommendations</b> with compatibility percentages,
            explanations, and the skills you'd need to build.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    name = st.text_input("Enter your name to get started (optional):", value=st.session_state.user_name)
    st.session_state.user_name = name

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🚀 Start Assessment", use_container_width=True):
            go_to("assessment")
    with col2:
        with st.expander("View careers covered"):
            from careers_data import CAREERS
            for career in CAREERS:
                st.markdown(f"- {career}")


# ---------------------------------------------------------------------------
# PAGE: ASSESSMENT
# ---------------------------------------------------------------------------
def render_assessment():
    greeting = f", {st.session_state.user_name}" if st.session_state.user_name else ""
    st.markdown(f"## 📝 Career Assessment{greeting}")
    st.markdown(
        f"<p style='color:#1E5AA8;'>Answer honestly for the most accurate match. "
        f"There are {len(QUESTIONS)} quick questions.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    with st.form("assessment_form"):
        scores = render_questionnaire()
        submitted = st.form_submit_button("✅ See My Results", use_container_width=True)

    if submitted:
        st.session_state.user_scores = scores
        go_to("results")

    if st.button("⬅ Back to Home"):
        go_to("home")


# ---------------------------------------------------------------------------
# PAGE: RESULTS
# ---------------------------------------------------------------------------
def render_results():
    greeting = f", {st.session_state.user_name}" if st.session_state.user_name else ""
    st.markdown(f"## 🎯 Your Top Career Matches{greeting}")
    st.markdown(
        "<p style='color:#1E5AA8;'>Based on your responses, here are the "
        "technology careers that best fit your profile.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    user_scores = st.session_state.user_scores
    if not user_scores:
        st.warning("No assessment data found. Please take the assessment first.")
        if st.button("Go to Assessment"):
            go_to("assessment")
        return

    top_recommendations = get_top_recommendations(user_scores, top_n=3)

    medals = ["🥇", "🥈", "🥉"]
    for rank, (career_name, info) in enumerate(top_recommendations):
        percentage = info["percentage"]
        description = info["description"]
        skills = info["skills"]
        explanation = build_explanation(career_name, info["top_matches"])

        skill_chips = "".join(f"<span class='skill-chip'>{s}</span>" for s in skills)

        st.markdown(
            f"""
            <div class="career-card">
                <span class="career-rank-badge">{medals[rank]} #{rank + 1} Match</span>
                <h3>{career_name}</h3>
                <div class="compat-percentage">{percentage}% Compatible</div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(percentage / 100)
        st.markdown(
            f"""
                <p><b>About this career:</b> {description}</p>
                <p><b>Why it was recommended:</b><br>{explanation}</p>
                <p><b>Core skills required:</b><br>{skill_chips}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    with st.expander("📊 See compatibility scores for all 8 careers"):
        from recommendation import calculate_scores
        all_scores = calculate_scores(user_scores)
        sorted_all = sorted(all_scores.items(), key=lambda x: x[1]["percentage"], reverse=True)
        for career_name, info in sorted_all:
            st.write(f"**{career_name}** — {info['percentage']}%")
            st.progress(info["percentage"] / 100)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔁 Retake Assessment", use_container_width=True):
            go_to("assessment")
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "home"
            st.session_state.user_scores = None
            st.rerun()


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------
if st.session_state.page == "home":
    render_home()
elif st.session_state.page == "assessment":
    render_assessment()
elif st.session_state.page == "results":
    render_results()
