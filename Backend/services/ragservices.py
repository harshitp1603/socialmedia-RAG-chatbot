from services.vectorstore import search_chunks
from services.llmservice import llm

from services.memoryservice import (
    add_message,
    get_history
)


def ask_rag(question):

    results = search_chunks(question)

    documents = results["documents"][0]
    metadata = results["metadatas"][0]

    context = "\n\n".join(documents)

    history = get_history()

    prompt = f"""
You are a social media video analyst.

Use previous conversation when relevant.

Previous Conversation:
{history}

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    add_message(
        "User",
        question
    )

    add_message(
        "Assistant",
        response.content
    )

    return {
        "answer": response.content,
        "sources": metadata
    }