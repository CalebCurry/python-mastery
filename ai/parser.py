from pathlib import Path

from init import connect
from unstructured.partition.md import partition_md
from unstructured.chunking.title import chunk_by_title

from embedder import embed


def parse_and_chunk(filepath):
    elements = partition_md(filepath)

    chunks = chunk_by_title(
        elements, max_characters=800, overlap=150, combine_text_under_n_chars=50
    )

    return chunks


# clear the db to reembed
conn = connect()
with conn.cursor() as cursor:
    cursor.execute("TRUNCATE embeddings")
    conn.commit()
    conn.close()

for file in sorted((Path(__file__).parent / "lessons").glob("*.md")):
    chunks = parse_and_chunk(file)

    current_title = "Unknown"
    for chunk in chunks:
        orig_elements = chunk.metadata.orig_elements
        titles = (
            [elem.text for elem in orig_elements if elem.category == "Title"]
            if orig_elements
            else []
        )
        if titles:
            title = titles[0]
            current_title = titles[0]
        else:
            title = current_title

        vector = embed([chunk.text])[0]
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO embeddings (embedding, section, lesson, content) VALUES (%s, %s, %s, %s)",
                (vector, title, chunk.metadata.filename, chunk.text),
            )
            conn.commit()
            conn.close()
        print(f"{chunk.metadata.filename} -> {title}")
        print(chunk.text[:30])
