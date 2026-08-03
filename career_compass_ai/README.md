# 🧭 CareerCompass AI

A **rule-based** AI Career Recommendation System built with Python and Streamlit.
Given a short assessment, it recommends the top 3 technology careers that best
match a user's interests, strengths, and preferred work style — using
transparent **weighted scoring and similarity logic**, with **no machine
learning models or external AI APIs**.

Built as an AI internship project to demonstrate rule-based recommendation
system design, modular Python architecture, and Streamlit UI development.

---

## ✨ Features

- 12-question assessment using sliders, radio buttons, and select boxes
- Measures: programming interest, math, problem solving, creativity,
  communication, AI interest, cybersecurity interest, hardware vs. software
  preference, teamwork, leadership, independence, and design sense
- Covers 8 technology careers: AI Engineer, Data Scientist, Software Engineer,
  Web Developer, Cybersecurity Analyst, Cloud Engineer, Embedded Systems
  Engineer, and UI/UX Designer
- Weighted scoring engine with a similarity-based match for the
  hardware/software preference attribute
- Top 3 recommendations with compatibility percentage, description,
  explanation ("why it was recommended"), and required skills
- Clean, modern, all-blue UI with cards and progress bars
- Fully modular codebase, organized across separate files

---

## 📁 Project Structure

```
career_compass_ai/
├── app.py              # Main Streamlit app: page routing (Home/Assessment/Results)
├── questionnaire.py     # Question bank + widget rendering logic
├── careers_data.py       # Career descriptions, required skills, and weight matrix
├── recommendation.py    # Rule-based weighted scoring & similarity engine
├── styles.py             # Custom CSS (blue-themed UI)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app.py
```

### 3. Use the app

1. **Home page** — brief intro, optionally enter your name, click "Start Assessment".
2. **Assessment page** — answer all 12 questions, then click "See My Results".
3. **Results page** — view your top 3 career matches with compatibility
   percentages, descriptions, explanations, and required skills. You can also
   expand a section to see scores for all 8 careers, or retake the assessment.

---

## 🧠 How the Recommendation Logic Works

1. Each question maps to one of 12 attributes (e.g. `programming`, `ai_interest`,
   `teamwork`), normalized to a **0–10 scale**.
2. Each of the 8 careers has a hand-tuned **weight vector** over these 12
   attributes (see `careers_data.py`), reflecting how important each trait is
   for that career.
3. For most attributes, the contribution to a career's score is simply
   `weight × user_score`.
4. For the **hardware vs. software** attribute specifically, we use a
   **similarity function** instead — because this attribute represents a
   *preference alignment* (how close the user is to a career's ideal point on
   the hardware-software spectrum), not a "higher is always better" trait.
5. Each career's total weighted score is normalized against its own maximum
   possible score to produce a **0–100% compatibility percentage**.
6. Careers are ranked by percentage, and the top 3 are shown along with the
   attributes that contributed most to that score (used to generate the
   "why it was recommended" explanation).

This entire pipeline is deterministic, explainable, and rule-based — no
neural networks, embeddings, or external AI calls are involved.

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** for the UI and app framework

---

## 📌 Notes for Extension

- To add a new career: add an entry to `CAREERS` in `careers_data.py` with a
  `description`, `skills`, `hw_target`, and `weights` dict.
- To add/change a question: edit the `QUESTIONS` list in `questionnaire.py`.
- To adjust how strongly an attribute affects a career: change its weight in
  `careers_data.py`.
