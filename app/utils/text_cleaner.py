import re


def clean_text(text: str) -> str:
    text = re.sub(r"[•●▪]", "-", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
