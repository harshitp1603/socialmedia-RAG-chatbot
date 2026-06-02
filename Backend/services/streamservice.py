from services.vectorstore import search_chunks
from services.llmservice import llm


def stream_rag(question):

    results = search_chunks(question)

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    prompt = f"""
You are a social media video analyst.

Context:
{context}

Question:
{question}

Answer:
"""

    for chunk in llm.stream(prompt):

        if chunk.content:
            yield chunk.content