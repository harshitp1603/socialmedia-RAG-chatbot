"use client";

import { useState } from "react";

export default function MemoryBox() {

  const [memory, setMemory] = useState<any[]>([]);

  async function loadMemory() {

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/memory"
      );

      const data = await response.json();

      setMemory(data);

    } catch (error) {

      console.error(error);

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
      🧠 Conversation Memory
    </h2>

    <button
      onClick={loadMemory}
      className="
      w-full
      py-3
      rounded-xl
      bg-gradient-to-r
      from-orange-500
      to-red-500
      font-semibold
      "
    >
      Refresh Memory
    </button>

    <div
      className="
      mt-5
      max-h-[300px]
      overflow-y-auto
      "
    >

      {memory.length === 0 ? (

        <p className="text-gray-400">
          No memory available yet.
        </p>

      ) : (

        memory.map((item, index) => (

          <div
            key={index}
            className="
            bg-black/20
            border border-white/10
            rounded-xl
            p-4
            mb-3
            "
          >
            <strong>
              {item.role}
            </strong>

            <p className="mt-2">
              {item.content}
            </p>

          </div>

        ))

      )}

    </div>

  </div>
  );
}