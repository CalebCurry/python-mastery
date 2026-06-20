from init import connect, settings
from openai import OpenAI
import psycopg

embedder = OpenAI(base_url=str(settings.embedder_base_url), api_key="example")


def embed_text(text: str):
    response = embedder.embeddings.create(model=settings.embedder_model, input=text)
    return response.data[0].embedding


def embed(text: list[str]):
    response = embedder.embeddings.create(model=settings.embedder_model, input=text)
    return [data.embedding for data in response.data]


phrases = [
    "The cat sleeps on the warm windowsill",
    "Coffee brewing in the morning sunlight",
    "Raindrops falling on autumn leaves",
    "Children playing in the neighborhood park",
    "Fresh bread cooling on the kitchen counter",
    "Birds singing at dawn's first light",
    "Ocean waves crashing against rocky shores",
    "Snow covering the mountain peaks",
    "Books stacked high on wooden shelves",
    "Garden flowers blooming in springtime",
    "Train whistling through the countryside",
    "Stars twinkling in the midnight sky",
    "Dogs barking at passing strangers",
    "Wind chimes dancing in the breeze",
    "Pizza delivery arriving just in time",
    "Thunder rumbling across dark clouds",
    "Bicycle wheels spinning down the path",
    "Campfire crackling under starry skies",
    "Music drifting from an open window",
    "Leaves rustling in the autumn wind",
]

# insert many
# vectors = embed(phrases)
# conn = connect()
# with conn.cursor() as cursor:
#     for content, vector in zip(phrases, vectors):
#         cursor.execute(
#             "INSERT INTO embeddings (embedding, section, lesson, content) VALUES (%s, %s, %s, %s)",
#             (vector, "test section", "test lesson", content),
#         )
#     conn.commit()
#     conn.close()


# insert one
# content = "The plant needs watered twice a day"
# vector = embed([content])[0]
# conn = connect()
# with conn.cursor() as cursor:
#     cursor.execute(
#         "INSERT INTO embeddings (embedding, section, lesson, content) VALUES (%s, %s, %s, %s)",
#         (vector, "test section", "test lesson", content),
#     )
#     conn.commit()
#     conn.close()

search = "The plant needs watered twice a day"

vector = embed([search])[0]
conn = connect()
with conn.cursor() as cursor:
    cursor.execute(
        """
        SELECT content, section, lesson, embedding <=> %s::vector as distance 
        FROM embeddings
        ORDER BY embedding <=> %s::vector 
        LIMIT 10
        """,
        (vector, vector),
    )

    result = cursor.fetchall()
    conn.close()

    for r in result:
        print(r)
