"use client";

import { useState } from "react";

export default function UploadForm() {
  const [url, setUrl] = useState("");
  const [videoId, setVideoId] = useState("A");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [platform, setPlatform] =useState("youtube");

  async function handleUpload() {
    setLoading(true);
    setMessage("");

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/ingest",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            url,
            platform,
            video_id: videoId
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {

        setMessage(
          ` ${data.detail}`
        );

        return;
      }

      setMessage(
        `😃 Video ${videoId} ingested successfully`
      );

      console.log(data);

    } catch (error) {

      setMessage(
        "😭 Backend connection failed"
      );

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
      hover:border-blue-500/30
      transition-all
      duration-300
    "
    >

    <h2 className="text-2xl font-bold mb-5">
      📤 Upload Video
    </h2>

    <input
      type="text"
      placeholder="Paste YouTube or Instagram URL"
      value={url}
      onChange={(e) => setUrl(e.target.value)}
      className="
      w-full
      p-3
      rounded-xl
      bg-black/20
      border border-white/10
      outline-none
      mb-4
      "
    />

    <select
      value={platform}
      onChange={(e) => setPlatform(e.target.value)}
      className="
      w-full
      p-3
      rounded-xl
      bg-black/20
      border border-white/10
      mb-4
      "
    >
      <option value="youtube">YouTube</option>
      <option value="instagram">Instagram</option>
    </select>

    <select
      value={videoId}
      onChange={(e) => setVideoId(e.target.value)}
      className="
      w-full
      p-3
      rounded-xl
      bg-black/20
      border border-white/10
      mb-4
      "
    >
      <option value="A">Video A</option>
      <option value="B">Video B</option>
    </select>

    <button
      onClick={handleUpload}
      disabled={loading}
      className="
      w-full
      py-3
      rounded-xl
      bg-gradient-to-r
      from-blue-500
      to-purple-500
      font-semibold
      hover:scale-[1.02]
      transition-all
      "
    >
      {loading ? "Uploading..." : "Ingest Video"}
    </button>

    {message && (
      <p className="mt-4 text-sm text-gray-300">
        {message}
      </p>
    )}

  </div>
  );
}