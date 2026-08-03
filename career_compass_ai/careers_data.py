"""
careers_data.py
----------------
Static data module for CareerCompass AI.

Holds:
    - The list of attributes the assessment measures.
    - The career catalogue (description + required skills).
    - The weight matrix used by the rule-based recommendation engine.

Keeping all "knowledge" in one module makes it trivial to add a new
career or tweak a weight without touching the app or scoring logic.
"""

# ---------------------------------------------------------------------------
# Attributes measured by the questionnaire.
# Every attribute is scored on a 0-10 scale after normalization
# (see questionnaire.py for how raw widget values are converted).
# ---------------------------------------------------------------------------
ATTRIBUTES = [
    "programming",
    "math",
    "problem_solving",
    "creativity",
    "communication",
    "ai_interest",
    "cybersecurity",
    "hardware_software",   # 0 = pure software lover, 10 = pure hardware lover
    "teamwork",
    "leadership",
    "independence",        # 0 = prefers teams, 10 = prefers solo/independent work
    "design_sense",
]

# Human-readable labels used in charts / debug views.
ATTRIBUTE_LABELS = {
    "programming": "Programming Interest",
    "math": "Mathematics & Analytics",
    "problem_solving": "Problem Solving",
    "creativity": "Creativity",
    "communication": "Communication",
    "ai_interest": "AI / ML Interest",
    "cybersecurity": "Cybersecurity Interest",
    "hardware_software": "Hardware Affinity",
    "teamwork": "Teamwork",
    "leadership": "Leadership",
    "independence": "Independent Work Style",
    "design_sense": "Design / Aesthetic Sense",
}

# ---------------------------------------------------------------------------
# Career catalogue.
# `hw_target` is the ideal hardware_software score for that career
# (0 = fully software-oriented, 10 = fully hardware-oriented). It is used
# with a similarity function instead of a plain weight, because for this
# attribute "closer to the career's ideal" matters more than "higher is
# better".
# ---------------------------------------------------------------------------
CAREERS = {
    "AI Engineer": {
        "description": (
            "Designs, builds, and deploys intelligent systems and machine "
            "learning models that solve real-world problems, from computer "
            "vision to natural language processing."
        ),
        "skills": [
            "Python", "Machine Learning", "Deep Learning",
            "Mathematics & Statistics", "Data Structures", "Model Deployment",
        ],
        "hw_target": 1,
        "weights": {
            "programming": 9, "math": 9, "problem_solving": 8, "creativity": 6,
            "communication": 4, "ai_interest": 10, "cybersecurity": 2,
            "teamwork": 5, "leadership": 3, "independence": 6, "design_sense": 2,
        },
    },
    "Data Scientist": {
        "description": (
            "Extracts insights and trends from large datasets using "
            "statistics, visualization, and analytical modeling to guide "
            "business decisions."
        ),
        "skills": [
            "Python/R", "Statistics", "Data Visualization",
            "SQL", "Machine Learning Basics", "Storytelling with Data",
        ],
        "hw_target": 0,
        "weights": {
            "programming": 7, "math": 10, "problem_solving": 9, "creativity": 5,
            "communication": 7, "ai_interest": 7, "cybersecurity": 2,
            "teamwork": 6, "leadership": 4, "independence": 5, "design_sense": 3,
        },
    },
    "Software Engineer": {
        "description": (
            "Designs, develops, and maintains robust software applications "
            "and systems, following solid engineering and architectural "
            "principles."
        ),
        "skills": [
            "Data Structures & Algorithms", "OOP", "System Design",
            "Version Control (Git)", "Testing & Debugging", "APIs",
        ],
        "hw_target": 1,
        "weights": {
            "programming": 10, "math": 6, "problem_solving": 9, "creativity": 4,
            "communication": 5, "ai_interest": 3, "cybersecurity": 3,
            "teamwork": 7, "leadership": 4, "independence": 4, "design_sense": 2,
        },
    },
    "Web Developer": {
        "description": (
            "Builds and maintains websites and web applications, balancing "
            "front-end user experience with back-end functionality."
        ),
        "skills": [
            "HTML/CSS/JavaScript", "React or similar framework",
            "REST APIs", "Responsive Design", "Basic Backend (Node/Django)",
        ],
        "hw_target": 0,
        "weights": {
            "programming": 8, "math": 3, "problem_solving": 6, "creativity": 7,
            "communication": 5, "ai_interest": 2, "cybersecurity": 3,
            "teamwork": 6, "leadership": 3, "independence": 4, "design_sense": 7,
        },
    },
    "Cybersecurity Analyst": {
        "description": (
            "Protects systems, networks, and data from digital threats by "
            "monitoring, detecting, and responding to security incidents."
        ),
        "skills": [
            "Networking", "Ethical Hacking Basics", "Risk Assessment",
            "Security Tools (SIEM, Firewalls)", "Cryptography Basics",
        ],
        "hw_target": 4,
        "weights": {
            "programming": 5, "math": 5, "problem_solving": 9, "creativity": 3,
            "communication": 5, "ai_interest": 2, "cybersecurity": 10,
            "teamwork": 5, "leadership": 4, "independence": 6, "design_sense": 1,
        },
    },
    "Cloud Engineer": {
        "description": (
            "Designs, deploys, and manages scalable cloud infrastructure "
            "and services, ensuring reliability, security, and performance."
        ),
        "skills": [
            "AWS/Azure/GCP", "Linux", "Docker & Kubernetes",
            "Networking", "CI/CD Pipelines", "Infrastructure as Code",
        ],
        "hw_target": 3,
        "weights": {
            "programming": 7, "math": 5, "problem_solving": 8, "creativity": 3,
            "communication": 4, "ai_interest": 3, "cybersecurity": 6,
            "teamwork": 5, "leadership": 4, "independence": 5, "design_sense": 1,
        },
    },
    "Embedded Systems Engineer": {
        "description": (
            "Develops firmware and hardware-software integrated systems for "
            "devices such as sensors, robotics, and IoT products."
        ),
        "skills": [
            "C/C++", "Microcontrollers (Arduino/STM32)", "Circuit Design",
            "RTOS Basics", "Sensors & Actuators", "Debugging Hardware",
        ],
        "hw_target": 9,
        "weights": {
            "programming": 7, "math": 7, "problem_solving": 8, "creativity": 4,
            "communication": 3, "ai_interest": 2, "cybersecurity": 3,
            "teamwork": 4, "leadership": 3, "independence": 6, "design_sense": 2,
        },
    },
    "UI/UX Designer": {
        "description": (
            "Crafts intuitive, visually engaging, and user-centered "
            "interfaces and experiences for digital products."
        ),
        "skills": [
            "Wireframing & Prototyping (Figma)", "User Research",
            "Visual Design Principles", "Interaction Design", "Usability Testing",
        ],
        "hw_target": 0,
        "weights": {
            "programming": 3, "math": 2, "problem_solving": 6, "creativity": 10,
            "communication": 8, "ai_interest": 1, "cybersecurity": 1,
            "teamwork": 7, "leadership": 4, "independence": 3, "design_sense": 10,
        },
    },
}
