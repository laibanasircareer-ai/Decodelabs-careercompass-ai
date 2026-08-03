# 🧭 CareerCompass AI

A **rule-based AI Career Recommendation System** built with **Python** and **Streamlit**.

CareerCompass AI helps users discover the technology career that best matches their interests, strengths, and working style through a short assessment. Instead of using machine learning models, it relies on **transparent weighted scoring** and **similarity-based recommendation logic**, making every recommendation explainable and easy to understand.

Built as an AI internship project to demonstrate recommendation system design, modular Python architecture, and Streamlit application development.

---

## ✨ Features

- 12-question career assessment using sliders, radio buttons, and select boxes
- Evaluates programming interest, mathematics, problem solving, creativity, communication, AI interest, cybersecurity interest, hardware vs. software preference, teamwork, leadership, independence, and design sense
- Covers 8 in-demand technology careers:
  - AI Engineer
  - Data Scientist
  - Software Engineer
  - Web Developer
  - Cybersecurity Analyst
  - Cloud Engineer
  - Embedded Systems Engineer
  - UI/UX Designer
- Rule-based recommendation engine using weighted scoring and similarity matching
- Displays the **Top 3 career recommendations**
- Compatibility percentages for each recommendation
- Personalized explanation of why each career was recommended
- Required skills for every recommended career
- Clean, modern blue-themed Streamlit interface
- Modular and maintainable Python codebase

---

## 🌐 Live Demo

Experience CareerCompass AI directly in your browser—no installation required.

🔗 **Live Application:**  
https://decodelabs-careercompass-ai-vlbajjhm5vuukd2khxehhb.streamlit.app/

### Try it yourself

1. Enter your name (optional).
2. Complete the 12-question career assessment.
3. Instantly receive your **Top 3 Technology Career Recommendations**.
4. Explore your compatibility scores, personalized explanations, and the key skills required for each recommended career.

> **Note:** This application is deployed on **Streamlit Community Cloud**. The initial load may take a few seconds if the app has been inactive.

---

# 📸 UI Showcase

> Replace the image paths below with screenshots of your application.

### 🏠 Home Page

<img width="1918" height="976" alt="Screenshot 2026-08-03 205613" src="https://github.com/user-attachments/assets/ba4ed529-c240-453c-971c-ef4768f2769d" />

---

### 📝 Career Assessment

<img width="1912" height="990" alt="image" src="https://github.com/user-attachments/assets/4da23d4b-48c7-4fd8-af42-193ee4eec54a" />

---

### 📊 Recommendation Results

<img width="1919" height="993" alt="image" src="https://github.com/user-attachments/assets/7f75796d-762a-4cdc-8701-bedb6f706497" />
<img width="1919" height="974" alt="image" src="https://github.com/user-attachments/assets/99700fba-25d2-4ded-8a00-4d7a90211eaa" />

---

## 📁 Project Structure

```text
career_compass_ai/
├── app.py                      # Main Streamlit application
├── questionnaire.py            # Assessment questions and input widgets
├── careers_data.py             # Career database, skills, and weight matrix
├── recommendation.py           # Rule-based recommendation engine
├── styles.py                   # Custom CSS styling and UI theme
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
│
└── .streamlit/
    └── config.toml             # Streamlit theme configuration (light mode)
```
---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
streamlit run app.py
```

### 3. Use the Application

1. Open the Home page.
2. Enter your name (optional) and start the assessment.
3. Answer all 12 questions.
4. View your Top 3 career recommendations.
5. Explore compatibility percentages, recommendation explanations, and required skills.

---

## 🧠 How the Recommendation Engine Works

The recommendation system follows a fully deterministic and explainable pipeline:

1. Every assessment question maps to one of **12 user traits** (for example, programming, teamwork, AI interest, leadership, etc.).
2. Every technology career has its own **weighted profile** representing the importance of each trait.
3. User responses are normalized onto a **0–10 scale**.
4. Weighted scores are calculated for every career.
5. The **Hardware vs. Software** preference uses a similarity function instead of direct scoring because it represents preference alignment rather than skill level.
6. Scores are normalized into **compatibility percentages**.
7. Careers are ranked, and the **Top 3 recommendations** are presented along with explanations and required skills.

The entire recommendation engine is **rule-based**, **transparent**, and **explainable**.

No machine learning models, neural networks, embeddings, or external AI APIs are used.

---

## 🛠️ Tech Stack

- Python 3.9+
- Streamlit

---

## 📌 Future Improvements

- Add additional technology careers
- Expand the assessment questionnaire
- Export recommendations as a PDF report
- User accounts and saved assessments
- Personalized learning roadmap
- Online deployment using Streamlit Community Cloud

---

## 📌 Notes for Extension

- Add a new career by creating a new entry inside the `CAREERS` dictionary in `careers_data.py`.
- Add new assessment questions by updating the `QUESTIONS` list in `questionnaire.py`.
- Adjust recommendation behavior by modifying career weights inside `careers_data.py`.

---

# 🎯 Project Information

**Internship:** DecodeLabs Artificial Intelligence Internship

**Project:** Project 3 – AI Recommendation Logic

This project demonstrates the implementation of a **rule-based recommendation system** using weighted scoring and similarity matching to recommend suitable technology careers based on user preferences.

---

# 👩‍💻 Author

**Laiba Nasir**

Built as **Project 3** for the **DecodeLabs Artificial Intelligence Internship**.

If you found this project interesting, feel free to ⭐ the repository and connect with me on LinkedIn.
