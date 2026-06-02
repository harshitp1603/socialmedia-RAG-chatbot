from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def transcribe_video(video_path):

    segments, _ = model.transcribe(
        video_path
    )

    return " ".join(
        segment.text
        for segment in segments
    )