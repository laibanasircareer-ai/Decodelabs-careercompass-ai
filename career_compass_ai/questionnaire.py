"""
questionnaire.py
----------------
Defines the assessment questions and renders them as Streamlit widgets.

Each question is described declaratively (type, label, options, and a
mapping function that converts the raw widget answer into a normalized
0-10 score for one or more attributes from careers_data.ATTRIBUTES).

This keeps app.py free of widget-building logic and makes it easy to
add/remove/edit questions in one place.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Question bank
# ---------------------------------------------------------------------------
# Each entry is a dict with:
#   key        -> unique key, also used as the Streamlit widget key
#   type       -> "slider" | "radio" | "selectbox"
#   label      -> question text shown to the user
#   attribute  -> which ATTRIBUTES key this question feeds into
#   options    -> for radio/selectbox: list of (display_text, score) tuples
#   help       -> optional helper text
# ---------------------------------------------------------------------------

QUESTIONS = [
    {
        "key": "q_programming",
        "type": "slider",
        "label": "1. How much do you enjoy writing code / programming?",
        "attribute": "programming",
        "help": "1 = Not at all, 10 = I could code all day.",
    },
    {
        "key": "q_math",
        "type": "slider",
        "label": "2. How comfortable are you with mathematics, logic, and analytical reasoning?",
        "attribute": "math",
        "help": "1 = I avoid math, 10 = I love working with numbers and logic.",
    },
    {
        "key": "q_problem_solving",
        "type": "radio",
        "label": "3. When you face a difficult problem, what's your first instinct?",
        "attribute": "problem_solving",
        "options": [
            ("Break it into smaller steps and solve methodically", 10),
            ("Search for similar solved examples and adapt them", 7),
            ("Discuss it with others to brainstorm ideas", 6),
            ("Try random things until something works", 4),
        ],
    },
    {
        "key": "q_creativity",
        "type": "slider",
        "label": "4. How would you rate your creativity and out-of-the-box thinking?",
        "attribute": "creativity",
        "help": "1 = Prefer clear instructions, 10 = I love inventing new ideas.",
    },
    {
        "key": "q_communication",
        "type": "slider",
        "label": "5. How confident are you presenting or explaining ideas to others?",
        "attribute": "communication",
        "help": "1 = I prefer not to, 10 = I enjoy public speaking / explaining.",
    },
    {
        "key": "q_ai_interest",
        "type": "radio",
        "label": "6. How interested are you in Artificial Intelligence & Machine Learning?",
        "attribute": "ai_interest",
        "options": [
            ("Extremely interested, I actively study it", 10),
            ("Interested, I've done a few projects", 7),
            ("Somewhat curious but haven't explored much", 4),
            ("Not really interested", 1),
        ],
    },
    {
        "key": "q_cybersecurity",
        "type": "slider",
        "label": "7. How interested are you in cybersecurity, ethical hacking, or digital forensics?",
        "attribute": "cybersecurity",
        "help": "1 = No interest, 10 = Very passionate about security.",
    },
    {
        "key": "q_hardware_software",
        "type": "selectbox",
        "label": "8. Which do you enjoy working with more?",
        "attribute": "hardware_software",
        "options": [
            ("Purely software (code, apps, algorithms)", 0),
            ("Mostly software, a little hardware", 3),
            ("An equal mix of hardware and software", 5),
            ("Mostly hardware, a little software", 7),
            ("Purely hardware (circuits, sensors, devices)", 10),
        ],
    },
    {
        "key": "q_teamwork",
        "type": "slider",
        "label": "9. How much do you enjoy collaborating with a team?",
        "attribute": "teamwork",
        "help": "1 = I prefer working alone, 10 = I thrive in team settings.",
    },
    {
        "key": "q_leadership",
        "type": "radio",
        "label": "10. In group projects, which role do you naturally take?",
        "attribute": "leadership",
        "options": [
            ("I lead and coordinate the team", 10),
            ("I take charge of a specific module and guide others in it", 7),
            ("I contribute solidly but let others lead", 4),
            ("I prefer to follow clear instructions", 2),
        ],
    },
    {
        "key": "q_independence",
        "type": "selectbox",
        "label": "11. What is your preferred work style?",
        "attribute": "independence",
        "options": [
            ("Fully independent, deep focus work", 10),
            ("Mostly independent with occasional check-ins", 7),
            ("A balanced mix of solo and team work", 5),
            ("Mostly collaborative, working closely with others", 3),
            ("Fully team-based, constant collaboration", 0),
        ],
    },
    {
        "key": "q_design_sense",
        "type": "slider",
        "label": "12. How much do you care about visual design, aesthetics, and user experience?",
        "attribute": "design_sense",
        "help": "1 = Function over form, 10 = I obsess over how things look and feel.",
    },
]


def render_questionnaire():
    """
    Renders all questions as Streamlit widgets and returns a dict of
    normalized scores keyed by attribute name (0-10 scale).

    Multiple questions targeting the same attribute (none currently, but
    supported) are averaged automatically.
    """
    attribute_scores = {}
    attribute_counts = {}

    total = len(QUESTIONS)
    for i, q in enumerate(QUESTIONS):
        # Simple progress indicator above each question.
        st.progress((i) / total)

        if q["type"] == "slider":
            raw = st.slider(
                q["label"], min_value=1, max_value=10, value=5,
                help=q.get("help"), key=q["key"],
            )
            score = float(raw)

        elif q["type"] == "radio":
            labels = [opt[0] for opt in q["options"]]
            choice = st.radio(q["label"], labels, key=q["key"])
            score = dict(q["options"])[choice]

        elif q["type"] == "selectbox":
            labels = [opt[0] for opt in q["options"]]
            # Default to the middle option for a neutral starting point.
            default_index = len(labels) // 2
            choice = st.selectbox(
                q["label"], labels, index=default_index, key=q["key"]
            )
            score = dict(q["options"])[choice]

        else:
            continue

        attr = q["attribute"]
        attribute_scores[attr] = attribute_scores.get(attr, 0) + score
        attribute_counts[attr] = attribute_counts.get(attr, 0) + 1

        st.markdown("<div style='margin-bottom: 1.2rem;'></div>", unsafe_allow_html=True)

    # Average scores for attributes fed by more than one question.
    final_scores = {
        attr: attribute_scores[attr] / attribute_counts[attr]
        for attr in attribute_scores
    }
    return final_scores
