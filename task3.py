# DecodeLabs | Batch 2026
# Project 3: Universal Interactive AI Recommendation Engine
# Author: Alishba Ghulam Rasool

import numpy as np

# ==========================
# UNIVERSAL VOCABULARY
# ==========================

VOCABULARY = [
    # Technology
    "Python", "Algorithms", "Cloud Computing",
    "Data Science", "Automation", "Web Design",

    # Medical
    "Cardiology", "Neurology", "Surgery", "Anatomy",

    # Physics & Space
    "Quantum Physics", "Astrophysics",
    "Cosmology", "Rocketry",

    # Cooking & Gardening
    "Baking", "Gourmet Cooking",
    "Food Science", "Horticulture",
    "Organic Gardening",

    # Fashion
    "Fashion Designing",
    "Apparel Styling",
    "Haute Couture"
]

# ==========================
# DATABASE
# ==========================

ITEMS_DATABASE = [

    {
        "id": 1,
        "title": "DecodeLabs AI Predictive Algorithm Bootcamp",
        "category": "Technology",
        "tags": ["Python", "Algorithms", "Data Science"]
    },

    {
        "id": 2,
        "title": "Enterprise Cloud Architecture & Automation",
        "category": "Technology",
        "tags": ["Cloud Computing", "Automation", "Python"]
    },

    {
        "id": 3,
        "title": "Frontend Web Design & UI Development",
        "category": "Technology",
        "tags": ["Web Design"]
    },

    {
        "id": 4,
        "title": "Advanced Clinical Cardiology & Surgery",
        "category": "Medical",
        "tags": ["Cardiology", "Surgery", "Anatomy"]
    },

    {
        "id": 5,
        "title": "Quantum Astrophysics & Deep Space Cosmology",
        "category": "Space Science",
        "tags": [
            "Quantum Physics",
            "Astrophysics",
            "Cosmology"
        ]
    },

    {
        "id": 6,
        "title": "Michelin-Star Culinary Arts",
        "category": "Cooking",
        "tags": [
            "Gourmet Cooking",
            "Food Science",
            "Baking"
        ]
    },

    {
        "id": 7,
        "title": "Commercial Horticulture Systems",
        "category": "Gardening",
        "tags": [
            "Horticulture",
            "Organic Gardening"
        ]
    },

    {
        "id": 8,
        "title": "Vogue Apparel Styling & Haute Couture",
        "category": "Fashion",
        "tags": [
            "Fashion Designing",
            "Apparel Styling",
            "Haute Couture"
        ]
    }
]


# ==========================
# MAIN FUNCTION
# ==========================

def run_recommendation_engine():

    print("=" * 70)
    print("     UNIVERSAL INTERACTIVE AI RECOMMENDATION ENGINE")
    print("=" * 70)

    print("\nAvailable Interests:\n")

    for tag in VOCABULARY:
        print("•", tag)

    print("\nEnter interests separated by commas")
    print("Example: Python, Data Science, Algorithms")

    user_input = input("\nYour Interests: ").strip()

    if not user_input:
        print("\n❌ No input entered.")
        return

    user_interests = [
        interest.strip()
        for interest in user_input.split(",")
        if interest.strip()
    ]

    # ==========================
    # USER VECTOR
    # ==========================

    user_vector = np.array([
        1 if tag.lower() in
        [u.lower() for u in user_interests]
        else 0
        for tag in VOCABULARY
    ])

    print("\nUser Vector:")
    print(user_vector)

    recommendations = []

    # ==========================
    # CALCULATE SIMILARITY
    # ==========================

    for item in ITEMS_DATABASE:

        item_vector = np.array([
            1 if tag in item["tags"] else 0
            for tag in VOCABULARY
        ])

        intersection = np.logical_and(
            user_vector,
            item_vector
        ).sum()

        union = np.logical_or(
            user_vector,
            item_vector
        ).sum()

        similarity = (
            intersection / union
            if union != 0
            else 0
        )

        if similarity > 0:

            common_tags = [
                tag
                for tag in item["tags"]
                if tag.lower() in
                [u.lower() for u in user_interests]
            ]

            recommendations.append(
                (similarity, item, common_tags)
            )

    # ==========================
    # NO MATCH FOUND
    # ==========================

    if not recommendations:
        print("\n⚠ No recommendations found.")
        return

    # ==========================
    # SORT BY SCORE
    # ==========================

    recommendations.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    # ==========================
    # BEST RECOMMENDATION
    # ==========================

    best = recommendations[0]

    print("\n" + "=" * 70)
    print("🏆 BEST RECOMMENDATION")
    print("=" * 70)

    print("Title:", best[1]["title"])
    print("Category:", best[1]["category"])
    print("Score:", round(best[0] * 100, 2), "%")

    # ==========================
    # ALL RECOMMENDATIONS
    # ==========================

    print("\n" + "=" * 70)
    print("ALL MATCHING RECOMMENDATIONS")
    print("=" * 70)

    rank = 1

    for similarity, item, common_tags in recommendations:

        score = round(similarity * 100, 2)

        bar = "█" * int(score / 5)

        print(f"\n#{rank}")
        print("Title:", item["title"])
        print("Category:", item["category"])
        print("Match Score:", score, "%")
        print("Score Bar:", bar)

        print("Recommended Because:")

        for tag in common_tags:
            print("✓", tag)

        print("-" * 70)

        rank += 1


# ==========================
# RUN PROGRAM
# ==========================

if __name__ == "__main__":
    run_recommendation_engine()
