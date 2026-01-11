import spacy

nlp = spacy.load("en_core_web_sm")


def analyze_job_description(jd_text: str) -> dict:
    doc = nlp(jd_text)

    keywords = {token.text.lower() for token in doc if token.pos_ in {"NOUN", "PROPN"}}

    return {"keywords": sorted(keywords)}
