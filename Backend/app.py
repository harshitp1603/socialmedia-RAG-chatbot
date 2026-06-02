from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.ingest import router as ingest_router
from routers.chat import router as chat_router


app = FastAPI(title="Social Video RAG")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "Backend Running"}