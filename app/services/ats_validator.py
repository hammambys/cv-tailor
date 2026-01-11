FORBIDDEN_PATTERNS = ["|", "●", "▪", "table", "<table>"]


def validate_ats(text: str) -> bool:
    lowered = text.lower()
    return not any(pattern in lowered for pattern in FORBIDDEN_PATTERNS)
