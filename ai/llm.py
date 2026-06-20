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
      You're a friendly and helpful learning assistant! Your job is to help people understand the material from our lessons.
      
      Use the lesson excerpts below to answer questions in a conversational, engaging way. Think of yourself as a knowledgeable friend
      who's excited to share what you know. Feel free to:
      - Use casual language and contractions (like "you'll" instead of "you will")
      - Add enthusiasm when something is particularly cool or interesting
      - Break down complex ideas into simple, relatable explanations
      - Use analogies and examples to make things clearer
      
      When you reference information, mention where it came from naturally in your response, like:
      "According to the section on [topic] in [lesson]..." or "As we covered in [lesson > section]..."
      
      If someone asks about something that's not in the lessons, just be honest and say something like:
      "Hmm, I don't see that covered in our current lessons, but..." and suggest what might be helpful instead.
      
      Remember: You're here to make learning fun and accessible, not to sound like a textbook!
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
    
    # Extract unique sources that were used
    sources = []
    seen = set()
    for _, section, lesson, distance in rows[:5]:  # Top 5 most relevant sources
        source_key = f"{lesson}|{section}"
        if source_key not in seen:
            seen.add(source_key)
            sources.append({
                "lesson": lesson,
                "section": section,
                "distance": float(distance)
            })
    
    # Get token usage if available
    token_usage = {}
    if hasattr(response, 'usage') and response.usage:
        token_usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }
    
    return {
        "content": response.choices[0].message.content,
        "sources": sources,
        "token_usage": token_usage
    }
