from init import settings
from openai import OpenAI
import psycopg

embedder = OpenAI(base_url=str(settings.embedder_base_url), api_key="example")


def embed_text(text: str):
    response = embedder.embeddings.create(model=settings.embedder_model, input="text")
    return response.data[0].embedding


print(embed_text("hello"))
