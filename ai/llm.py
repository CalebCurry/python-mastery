from openai import OpenAI
from ai.embedder import embed
from ai.init import connect, settings

llm = OpenAI(base_url=str(settings.llm_base_url), api_key="example")


def search(search_string: str):
    vector = embed([search_string])[0]
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

        return result


def answer(question: str):
    rows = search(question)

    system = """
      Answer the prompt using only the relevant information from the lesson excerpts below.
      Each excerpt will be of the format [lesson > section]. Don't JUST give the source, but use the source to craft an answer and cite.
      Respond saying which section your answer came from following this format, like [lesson01 > How to water plants] (distance)
      If the answer is not in the excerpts explicitly say so. Avoid general knowledge and source everything. 
    """

    context = "\n\n".join(
        [
            f"[{lesson} > {section}] ({distance}) {content}"
            for content, section, lesson, distance in rows
        ]
    )

    # print(system + context)
    response = llm.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {"role": "system", "content": system + context},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content
