import yt_dlp

from faster_whisper import WhisperModel


def download_reel(url):

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


def transcribe_reel(video_path):

    model = WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        video_path
    )

    transcript = ""

    for segment in segments:

        transcript += (
            segment.text + " "
        )

    return transcript


def get_reel_metadata(url):

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

        return {
            "title": info.get("title"),
            "creator": info.get("uploader"),
            "views": info.get("view_count", 0),
            "duration": info.get("duration", 0)
        }