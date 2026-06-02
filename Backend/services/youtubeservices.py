import re
import yt_dlp

from faster_whisper import WhisperModel


# Load Whisper once when server starts
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def extract_video_id(url: str):

    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"

    match = re.search(
        pattern,
        url
    )

    if match:
        return match.group(1)

    return None


def download_youtube_video(url):

    ydl_opts = {
        "outtmpl": "temp/%(id)s.%(ext)s",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        info = ydl.extract_info(
            url,
            download=True
        )

        filename = ydl.prepare_filename(
            info
        )

    return filename


def transcribe_youtube_video(
    video_path
):

    segments, info = model.transcribe(
        video_path
    )

    transcript = ""

    for segment in segments:

        transcript += (
            segment.text + " "
        )

    if not transcript.strip():

        raise Exception(
            "Transcript is empty"
        )

    return transcript


def get_video_metadata(url: str):

    ydl_opts = {
        "quiet": True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        info = ydl.extract_info(
            url,
            download=False
        )

        likes = (
            info.get("like_count")
            or 0
        )

        comments = (
            info.get("comment_count")
            or 0
        )

        views = (
            info.get("view_count")
            or 1
        )

        engagement_rate = (
            (likes + comments)
            / views
        ) * 100

        return {
            "title": info.get("title"),
            "creator": info.get(
                "uploader"
            ),
            "views": views,
            "likes": likes,
            "comments": comments,
            "duration": info.get(
                "duration"
            ),
            "upload_date": info.get(
                "upload_date"
            ),
            "tags": info.get(
                "tags",
                []
            ),
            "engagement_rate": round(
                engagement_rate,
                2
            )
        }