"use client";

import { useState } from "react";

export default function ChatBox() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] =
  useState(false);

  async function askQuestion() {

    setLoading(true);
    setAnswer("");

    try {

        const response = await fetch(
        "http://127.0.0.1:8000/chat-stream",
        {
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify({
            question
            })
        }
        );

        if (!response.body) return;

        const reader =
        response.body.getReader();

        const decoder =
        new TextDecoder();

        while (true) {

        const {
            done,
            value
        } = await reader.read();

        if (done) break;

        const chunk =
            decoder.decode(value);

        setAnswer(
            prev => prev + chunk
        );
        }

    } catch (error) {

        console.error(error);

    } finally {

        setLoading(false);

    }
  }

  return (
  <div
    className="
    bg-white/5
    backdrop-blur-xl
    border border-white/10
    rounded-2xl
    p-6
    shadow-xl
    "
  >

    <h2 className="text-2xl font-bold mb-5">
      🤖 AI Chat
    </h2>

    <input
      type="text"
      placeholder="Ask anything about your videos..."
      value={question}
      onChange={(e) =>
        setQuestion(e.target.value)
      }
      className="
      w-full
      p-3
      rounded-xl
      bg-black/20
      border border-white/10
      mb-4
      "
    />

    <button
      onClick={askQuestion}
      disabled={loading}
      className="
      w-full
      py-3
      rounded-xl
      bg-gradient-to-r
      from-green-500
      to-emerald-600
      font-semibold
      "
    >
      {loading ? "Thinking..." : "Ask AI"}
    </button>

    <div
      className="
      mt-5
      bg-black/20
      border border-white/10
      rounded-xl
      p-4
      min-h-[180px]
      max-h-[300px]
      overflow-y-auto
      whitespace-pre-wrap
      "
    >
      {answer}
    </div>

  </div>
  );
}