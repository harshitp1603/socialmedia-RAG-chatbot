"use client";

import { useState } from "react";

export default function CompareBox() {

  const [videoA, setVideoA] =
    useState("A");

  const [videoB, setVideoB] =
    useState("B");

  const [question, setQuestion] =
    useState("");

  const [answer, setAnswer] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  async function compareVideos() {

    setLoading(true);
    setAnswer("");

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/compare",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json"
          },
          body: JSON.stringify({
            question,
            video_a: videoA,
            video_b: videoB,
          })
        }
      );

      const data =
        await response.json();

      setAnswer(data.answer);

    } catch (error) {

      console.error(error);

      setAnswer(
        "Comparison failed"
      );

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
      ⚖️ Compare Videos
    </h2>

    <div className="grid grid-cols-2 gap-3 mb-4">

      <select
        value={videoA}
        onChange={(e) =>
          setVideoA(e.target.value)
        }
        className="
        p-3
        rounded-xl
        bg-black/20
        border border-white/10
        "
      >
        <option value="A">Video A</option>
        <option value="B">Video B</option>
      </select>

      <select
        value={videoB}
        onChange={(e) =>
          setVideoB(e.target.value)
        }
        className="
        p-3
        rounded-xl
        bg-black/20
        border border-white/10
        "
      >
        <option value="A">Video A</option>
        <option value="B">Video B</option>
      </select>

    </div>

    <input
      type="text"
      placeholder="What should I compare?"
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
      onClick={compareVideos}
      disabled={loading}
      className="
      w-full
      py-3
      rounded-xl
      bg-gradient-to-r
      from-purple-500
      to-pink-500
      font-semibold
      "
    >
      {loading ? "Comparing..." : "Compare"}
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