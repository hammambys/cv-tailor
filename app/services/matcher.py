from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def score_text_against_jd(text_blocks: list[str], jd_text: str):
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    results = []
    for block in text_blocks:
        embedding = model.encode(block, convert_to_tensor=True)
        score = util.cos_sim(embedding, jd_embedding).item()
        results.append({"text": block, "score": round(score, 3)})

    return sorted(results, key=lambda x: x["score"], reverse=True)
