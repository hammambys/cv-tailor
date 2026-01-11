from fastapi import APIRouter, UploadFile, Form
import tempfile

from app.services.pdf_parser import extract_text_from_pdf, is_text_based
from app.services.text_cleaner import clean_text
from app.services.section_parser import split_sections

router = APIRouter(prefix="/cv", tags=["CV"])


@router.post("/tailor")
async def tailor_cv(cv: UploadFile, job_description: str = Form(...)):
    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await cv.read())
        pdf_path = tmp.name

    raw_text = extract_text_from_pdf(pdf_path)

    if not is_text_based(raw_text):
        return {"error": "Scanned or image-based PDF not supported"}

    cleaned_text = clean_text(raw_text)
    sections = split_sections(cleaned_text)

    return {"sections": sections, "job_description": job_description}
