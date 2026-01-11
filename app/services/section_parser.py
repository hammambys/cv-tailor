SECTION_HEADERS = {
    "summary",
    "experience",
    "education",
    "skills",
    "projects",
    "certifications",
}


def split_sections(text: str) -> dict:
    sections = {}
    current_section = "other"
    sections[current_section] = []

    for line in text.split("\n"):
        normalized = line.strip().lower()

        if normalized in SECTION_HEADERS:
            current_section = normalized
            sections[current_section] = []
        else:
            sections[current_section].append(line)

    return {
        section: "\n".join(lines).strip()
        for section, lines in sections.items()
        if lines
    }
