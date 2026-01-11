import pdfplumber

MIN_TEXT_LENGTH = 500


def extract_text_from_pdf(file_path: str) -> str:
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text).strip()


def is_text_based(text: str) -> bool:
    return len(text) >= MIN_TEXT_LENGTH
