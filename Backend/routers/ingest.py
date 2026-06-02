from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException

import json
import os

from services.youtubeservices import (
    download_youtube_video,
    transcribe_youtube_video,
    get_video_metadata
)

router = APIRouter()


class VideoInput(BaseModel):
    url: str
    platform: str
    video_id: str


@router.post("/ingest")
async def ingest_video(data: VideoInput):

    try:

        if data.platform == "youtube":

            file = download_youtube_video(
                data.url
            )

            try:

                transcript = (
                    transcribe_youtube_video(
                        file
                    )
                )

            finally:

                if os.path.exists(file):
                    os.remove(file)

            metadata = get_video_metadata(
                data.url
            )

        elif data.platform == "instagram":

            from services.instagramservices import (
                download_reel,
                transcribe_reel,
                get_reel_metadata
            )

            file = download_reel(
                data.url
            )

            try:

                transcript = transcribe_reel(
                    file
                )

            finally:

                if os.path.exists(file):
                    os.remove(file)

            metadata = get_reel_metadata(
                data.url
            )

        else:

            raise Exception(
                "Unsupported platform"
            )

        from services.vectorstore import (
            chunk_transcript,
            store_chunks,
            delete_video
        )

        chunks = chunk_transcript(
            transcript
        )

        delete_video(
            data.video_id
        )

        store_chunks(
            chunks,
            video_id=data.video_id,
            metadata=metadata
        )

        videos_file = "data/videos.json"

        if os.path.exists(
            videos_file
        ):

            try:

                with open(
                    videos_file,
                    "r"
                ) as f:

                    videos = json.load(f)

            except:

                videos = []

        else:

            videos = []

        videos = [

            v for v in videos

            if v["video_id"]
            != data.video_id
        ]

        videos.append({

            "video_id":
            data.video_id,

            "platform":
            data.platform,

            "title":
            metadata.get(
                "title"
            ),

            "creator":
            metadata.get(
                "creator"
            ),

            "views":
            metadata.get(
                "views"
            ),

            "duration":
            metadata.get(
                "duration"
            )
        })

        os.makedirs(
            "data",
            exist_ok=True
        )

        with open(
            videos_file,
            "w"
        ) as f:

            json.dump(
                videos,
                f,
                indent=2
            )

        return {

            "video_id":
            data.video_id,

            "platform":
            data.platform,

            "metadata":
            metadata,

            "transcript_length":
            len(transcript),

            "preview":
            transcript[:500]
        }

    except Exception as e:

        print(
            "\n========== INGEST ERROR =========="
        )

        print(type(e))
        print(e)

        print(
            "==================================\n"
        )

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/videos")
def get_videos():

    videos_file = "data/videos.json"

    if not os.path.exists(
        videos_file
    ):

        return []

    with open(
        videos_file,
        "r"
    ) as f:

        return json.load(f)


@router.get("/debug")
def debug():

    from services.vectorstore import collection

    return {
        "chunks_stored":
        collection.count()
    }


@router.get("/test-instagram")
def test_instagram():

    from services.instagramservices import (
        download_reel,
        transcribe_reel
    )

    file = download_reel(
        "https://www.instagram.com/reel/DV3EkrZk78O/"
    )

    transcript = transcribe_reel(
        file
    )

    print(
        "\n===== TRANSCRIPT ====="
    )

    print(
        transcript[:500]
    )

    print(
        "======================\n"
    )

    return {

        "file":
        file,

        "transcript":
        transcript[:1000]
    }