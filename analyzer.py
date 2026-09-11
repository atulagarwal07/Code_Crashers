def analyze_content(text):
    score = 100
    warnings = []

    text_lower = text.lower()

    # 1. Sensational language
    sensational_words = [
        "breaking",
        "shocking",
        "unbelievable",
        "you won't believe",
        "urgent"
    ]

    for word in sensational_words:
        if word in text_lower:
            score -= 15
            warnings.append("Sensational or alarming language detected")
            break

    # 2. Pressure to act
    pressure_words = [
        "act now",
        "share this",
        "share before",
        "click now",
        "limited time"
    ]

    for word in pressure_words:
        if word in text_lower:
            score -= 15
            warnings.append("Pressure or urgency detected")
            break

    # 3. Suspicious financial claims
    financial_words = [
        "free money",
        "guaranteed money",
        "₹50,000",
        "rs 50000",
        "win money",
        "get rich"
    ]

    for word in financial_words:
        if word in text_lower:
            score -= 25
            warnings.append("Unverified financial claim detected")
            break

    # 4. Health-related absolute claims
    health_words = [
        "100% cure",
        "guaranteed cure",
        "cures every disease",
        "miracle cure"
    ]

    for word in health_words:
        if word in text_lower:
            score -= 25
            warnings.append("Potentially misleading health claim detected")
            break

    # 5. Sharing pressure
    if "share" in text_lower:
        score -= 10
        warnings.append("Strong sharing pressure detected")

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    # Determine risk level
    if score >= 80:
        risk = "Low Risk"
    elif score >= 60:
        risk = "Moderate Risk"
    elif score >= 40:
        risk = "Suspicious"
    else:
        risk = "High Risk"

    # If no warning was found
    if not warnings:
        warnings.append("No major warning signs detected")

    return {
        "score": score,
        "risk": risk,
        "warnings": warnings
    }


# Test the analyzer
if __name__ == "__main__":
    test_text = "BREAKING!!! FREE MONEY! ACT NOW! SHARE THIS!!!"

    result = analyze_content(test_text)

    print("Trust Score:", result["score"])
    print("Risk Level:", result["risk"])
    print("Warnings:")

    for warning in result["warnings"]:
        print("-", warning)