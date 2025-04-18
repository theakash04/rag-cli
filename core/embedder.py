from mistralai import Mistral
from shared.config import API_KEY, EMBEDD_MODEL
import time



client = Mistral(api_key=API_KEY)

def get_text_embedding(text: str | list[str]):
    if isinstance(text, str):
        text = [text]

    response = client.embeddings.create(
        model=EMBEDD_MODEL,
        inputs=text
    )
    embeddings = [item.embedding for item in response.data]
    return embeddings[0] if len(embeddings) == 1 else embeddings


def embedd_chunks(chunks: list[str], delay: float = 3.0):
    embeddings = get_text_embedding(chunks)
    return embeddings
