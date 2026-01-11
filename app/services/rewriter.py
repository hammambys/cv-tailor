def build_rewrite_prompt(bullet: str, jd_text: str) -> str:
    return f"""
Rewrite the bullet point below to better align with the job description.

Rules:
- Do NOT add new skills, tools, or experience
- Keep ATS-friendly language
- One sentence only
- Start with an action verb

Job Description:
{jd_text}

Bullet:
{bullet}
""".strip()
