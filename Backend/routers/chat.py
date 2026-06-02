from fastapi import APIRouter
from pydantic import BaseModel

from services.ragservices import ask_rag
from services.comparisonservices import compare_videos
from fastapi.responses import StreamingResponse
from services.streamservice import stream_rag

router = APIRouter()


class ChatInput(BaseModel):
    question: str

class CompareInput(BaseModel):
    question: str
    video_a: str
    video_b: str


@router.post("/chat")
async def chat(data: ChatInput):

    return ask_rag(data.question)

@router.post("/compare")
async def compare(data: CompareInput):

    return {
        "answer": compare_videos(
            data.question,
            data.video_a,
            data.video_b
        )
    }

@router.get("/memory")
def memory():

    from services.memoryservice import (
        conversation_memory
    )

    return conversation_memory

@router.post("/chat-stream")
async def chat_stream(data: ChatInput):

    return StreamingResponse(
        stream_rag(data.question),
        media_type="text/plain"
    )