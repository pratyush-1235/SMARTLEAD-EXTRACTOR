def score_lead(name, title, description):
    title_lower = title.lower()

    if "ceo" in title_lower or "founder" in title_lower:
        return "High"
    elif "marketing" in title_lower or "sales" in title_lower:
        return "Medium"
    else:
        return "Low"
