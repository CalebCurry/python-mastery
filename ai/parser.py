from pathlib import Path

from unstructured.partition.md import partition_md
from unstructured.chunking.title import chunk_by_title


def parse_and_chunk(filepath):
    elements = partition_md(filepath)

    chunks = chunk_by_title(
        elements, max_characters=800, overlap=150, combine_text_under_n_chars=50
    )

    return chunks


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
        print(f"{chunk.metadata.filename} -> {title}")
        print(chunk.text[:30])
