from services.vectorstore import (
    search_chunks_by_video
)

from services.llmservice import llm

from services.memoryservice import (
    add_message,
    get_history
)


def compare_videos(question,video_a,video_b):

    a_results = search_chunks_by_video(
        question,
        video_a
    )

    b_results = search_chunks_by_video(
        question,
        video_b
    )

    a_context = "\n".join(
        a_results["documents"][0]
    )

    b_context = "\n".join(
        b_results["documents"][0]
    )

    history = get_history()

    prompt = f"""
You are a social media analyst.

Previous Conversation:
{history}

Video A:
{a_context}

Video B:
{b_context}

Question:
{question}

Compare both videos.
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

    return response.content