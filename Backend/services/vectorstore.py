from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="video_chunks"
)


def chunk_transcript(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_text(text)


def store_chunks(
    chunks,
    video_id,
    metadata=None
):

    if metadata is None:
        metadata = {}

    for i, chunk in enumerate(chunks):

        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[f"{video_id}_{i}"],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{
                "video_id": video_id,
                "chunk_id": i,
                "creator": str(
                    metadata.get("creator", "")
                ),
                "views": int(
                    metadata.get("views", 0)
                ),
                "likes": int(
                    metadata.get("likes", 0)
                ),
                "comments": int(
                    metadata.get("comments", 0)
                ),
                "engagement_rate": float(
                    metadata.get(
                        "engagement_rate",
                        0
                    )
                )
            }]
        )

def search_chunks(query, top_k=5):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results


def search_chunks_by_video(
    query,
    video_id,
    top_k=5
):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where={
            "video_id": video_id
        }
    )

    return results

def delete_video(video_id):

    collection.delete(
        where={
            "video_id": video_id
        }
    )