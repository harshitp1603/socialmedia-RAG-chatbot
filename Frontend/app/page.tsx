import UploadForm from "@/components/uploadform";
import ChatBox from "@/components/chatbox";
import CompareBox from "@/components/comparebox";
import MemoryBox from "@/components/memorybox";

export default function Home() {

  return (

    <main className="
      min-h-screen
      flex
      justify-center
      items-start
      text-white
      px-6
      py-10
    ">

      <div className="
        w-full
        max-w-4xl
      ">

        <div className="
          text-center
          mb-12
        ">

          <h1 className="
            text-6xl
            font-extrabold
            bg-gradient-to-r
            from-blue-400
            via-purple-400
            to-pink-400
            bg-clip-text
            text-transparent
            mb-3
          ">
            Social Media Chatbot
          </h1>

          <p className="
            text-gray-400
            text-lg
          ">
            Analyze YouTube & Instagram Videos with AI
          </p>

        </div>

        <div className="
          grid
          md:grid-cols-2
          gap-6
        ">

          <UploadForm />

          <ChatBox />

          <CompareBox />

          <MemoryBox />

        </div>

      </div>

    </main>

  );
}