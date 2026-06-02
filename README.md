#  Social Video Chatbot

AI-powered Social Media Video Analysis Platform that can analyze **YouTube Videos** and **Instagram Reels**, answer questions using **RAG (Retrieval-Augmented Generation)**, compare multiple videos, and maintain conversation memory.

##  Features

### Video Ingestion

* Ingest YouTube videos
* Ingest Instagram Reels
* Automatic video download
* Audio transcription using Whisper
* Metadata extraction

###  AI Chat

* Ask questions about uploaded videos
* Context-aware responses
* Streaming AI responses
* Conversation memory support

###  Video Comparison

* Compare Video A and Video B
* Cross-platform comparison

  * YouTube vs YouTube
  * Instagram vs Instagram
  * YouTube vs Instagram

###  Memory System

* Stores recent conversation history
* Context-aware follow-up questions

###  Vector Search

* ChromaDB vector storage
* Semantic search using embeddings
* Retrieval-Augmented Generation (RAG)

---

#  Tech Stack

## Backend

* FastAPI
* ChromaDB
* Sentence Transformers
* Faster Whisper
* yt-dlp
* OpenAI / Gemini
* Python

## Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

---

#  Architecture

```text
User
 │
 ▼
Frontend (Next.js)
 │
 ▼
FastAPI Backend
 │
 ├── YouTube / Instagram Ingestion
 │
 ├── Whisper Transcription
 │
 ├── Chunking
 │
 ├── ChromaDB Storage
 │
 └── RAG Retrieval
 │
 ▼
LLM (OpenAI / Gemini)
 │
 ▼
Answer
```

---

# Screenshots

## Main Dashboard
<img width="1856" height="782" alt="Screenshot 2026-06-02 231437" src="https://github.com/user-attachments/assets/e8a08632-a1c0-41e9-957d-fc8181407974" />

---

## Upload & AI Chat
<img width="1802" height="627" alt="Screenshot 2026-06-02 231452" src="https://github.com/user-attachments/assets/6d8629ff-72ed-468c-ab38-b9519b0454f6" />

---

## Compare Videos & Memory
<img width="1883" height="914" alt="Screenshot 2026-06-02 231505" src="https://github.com/user-attachments/assets/34ecd6a4-a910-43ed-a158-9241e6b8eb20" />

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/your-username/social-video-rag.git

cd social-video-rag
```

---

# Backend Setup

## Create Virtual Environment

```bash
cd backend

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create:

```text
backend/.env
```

Example:

```env
OPENAI_API_KEY=your_openai_api_key
```

or

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## Install FFmpeg

Whisper requires FFmpeg.

### Windows

Download:

https://ffmpeg.org/download.html

Add FFmpeg to PATH.

Verify:

```bash
ffmpeg -version
```

---

## Start Backend

```bash
uvicorn app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## Install Dependencies

```bash
cd frontend

npm install
```

---

## Run Frontend

```bash
npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

# Usage

## Upload Video

1. Paste YouTube URL or Instagram Reel URL
2. Select:

   * Video A
   * Video B
3. Click:

   * Ingest Video

---

## Ask Questions

Examples:

```text
What is Video A about?

Summarize the uploaded video.

What are the key points discussed?

Who is the creator of Video A?
```

---

## Compare Videos

Examples:

```text
Compare Video A and Video B.

Which video has better engagement?

What are the differences between the two videos?

Compare the tone of both videos.
```

---

## Memory

Click:

```text
Refresh Memory
```

to view stored conversation history.

