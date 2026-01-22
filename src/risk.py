def calculate_risk(row):
    """
    Calculate risk score based on severity and confidence
    """
    score = 20

    if row["severity"] == "high":
        score += 40
    elif row["severity"] == "medium":
        score += 20

    score += int(row["confidence"] * 0.3)

    return min(score, 100)
