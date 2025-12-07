def classify_ticket(description: str):
    text = description.lower()

    if "network" in text or "internet" in text:
        category = "Network"
    elif "password" in text or "login" in text:
        category = "Access"
    elif "error" in text or "bug" in text:
        category = "Application"
    else:
        category = "General"

    # simple priority rules
    if "urgent" in text or "not working" in text:
        priority = "High"
    elif "slow" in text:
        priority = "Medium"
    else:
        priority = "Low"

    return category, priority
