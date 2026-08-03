"""
recommendation.py
------------------
Rule-based recommendation engine for CareerCompass AI.

No machine learning models or external APIs are used. Instead, each
career has a hand-crafted weight vector over the assessment attributes.
We compute a weighted-dot-product compatibility score between the
user's normalized answers and each career's ideal profile, blend in a
similarity score for the hardware/software preference, normalize the
result to a 0-100% compatibility score, and return the ranked list.
"""

from careers_data import CAREERS, ATTRIBUTES


def _hardware_similarity(user_value: float, target_value: float) -> float:
    """
    Returns a 0-10 similarity score based on how close the user's
    hardware/software preference is to a career's ideal target.

    A perfect match (distance 0) scores 10; the maximum possible
    distance (10) scores 0. This rewards *alignment* rather than simply
    rewarding a high raw value, which is the correct behavior for a
    preference-style attribute.
    """
    distance = abs(user_value - target_value)
    return max(0.0, 10.0 - distance)


def calculate_scores(user_scores: dict) -> dict:
    """
    Calculates a compatibility score (0-100%) for every career.

    Args:
        user_scores: dict mapping attribute name -> normalized score (0-10)

    Returns:
        dict mapping career name -> {
            "percentage": float,
            "description": str,
            "skills": list[str],
            "top_matches": list[str]  # attributes that contributed most
        }
    """
    results = {}

    for career_name, career_info in CAREERS.items():
        weights = career_info["weights"]
        hw_target = career_info["hw_target"]

        weighted_sum = 0.0
        max_possible = 0.0
        contributions = []  # (attribute, contribution_value) for explainability

        for attr in ATTRIBUTES:
            weight = weights.get(attr, 0)
            user_value = user_scores.get(attr, 5)  # default neutral if missing

            if attr == "hardware_software":
                # Use similarity instead of a plain product, since this
                # attribute represents a preference alignment, not a
                # "more is always better" trait.
                similarity = _hardware_similarity(user_value, hw_target)
                contribution = weight * similarity
                max_possible += weight * 10.0
            else:
                contribution = weight * user_value
                max_possible += weight * 10.0

            weighted_sum += contribution
            contributions.append((attr, contribution))

        # Normalize to a percentage of the maximum achievable score for
        # this career's weight profile.
        percentage = (weighted_sum / max_possible) * 100 if max_possible > 0 else 0
        percentage = round(min(100.0, max(0.0, percentage)), 1)

        # Identify the top 3 contributing attributes for the "why" explanation.
        contributions.sort(key=lambda x: x[1], reverse=True)
        top_matches = [attr for attr, _ in contributions[:3]]

        results[career_name] = {
            "percentage": percentage,
            "description": career_info["description"],
            "skills": career_info["skills"],
            "top_matches": top_matches,
        }

    return results


def get_top_recommendations(user_scores: dict, top_n: int = 3) -> list:
    """
    Returns the top N careers sorted by compatibility percentage,
    highest first, as a list of (career_name, info_dict) tuples.
    """
    scored = calculate_scores(user_scores)
    ranked = sorted(scored.items(), key=lambda item: item[1]["percentage"], reverse=True)
    return ranked[:top_n]


def build_explanation(career_name: str, top_matches: list) -> str:
    """
    Builds a short, human-readable explanation of why a career was
    recommended, based on the attributes that contributed most to its
    score.
    """
    from careers_data import ATTRIBUTE_LABELS

    readable = [ATTRIBUTE_LABELS.get(a, a) for a in top_matches]

    if len(readable) == 1:
        joined = readable[0]
    elif len(readable) == 2:
        joined = f"{readable[0]} and {readable[1]}"
    else:
        joined = f"{', '.join(readable[:-1])}, and {readable[-1]}"

    return (
        f"Your profile aligns strongly with **{career_name}** mainly because of your "
        f"scores in **{joined}** — these are the exact traits this career depends on most."
    )
