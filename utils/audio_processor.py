
import yt_dlp
from pydub import AudioSegment
import os

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


# 1. Download YouTube audio
def download_youtube_audio(url: str) -> str:
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
            },
        ],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = os.path.splitext(
            ydl.prepare_filename(info)
        )[0] + ".wav"

    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"Downloaded WAV file not found: {filename}"
        )

    if os.path.getsize(filename) == 0:
        raise ValueError("Downloaded audio file is empty.")

    print(f"Downloaded audio: {filename}")
    return filename


# 2. Convert audio/video to WAV
def convert_to_wav(input_path: str) -> str:
    if not os.path.exists(input_path):
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )

    output_path = os.path.splitext(
        input_path
    )[0] + "_converted.wav"

    audio = AudioSegment.from_file(input_path)

    if len(audio) == 0:
        raise ValueError("Input audio has zero duration.")

    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    audio = audio.set_sample_width(2)

    audio.export(output_path, format="wav")

    if not os.path.exists(output_path):
        raise FileNotFoundError("WAV conversion failed.")

    print(f"Converted audio: {output_path}")
    print(f"Duration: {len(audio) / 1000:.2f} seconds")

    return output_path


# 3. Split audio into chunks
def chunk_audio(wav_path: str, chunk_minutes: int = 10) -> list:
    if not os.path.exists(wav_path):
        raise FileNotFoundError(
            f"WAV file not found: {wav_path}"
        )

    if chunk_minutes <= 0:
        raise ValueError("Chunk duration must be positive.")

    audio = AudioSegment.from_wav(wav_path)

    if len(audio) == 0:
        raise ValueError("Cannot split empty audio.")

    chunk_ms = chunk_minutes * 60 * 1000
    chunks = []

    for i, start in enumerate(range(0, len(audio), chunk_ms)):
        chunk = audio[start:start + chunk_ms]

        if len(chunk) == 0:
            continue

        chunk_path = f"{wav_path}_chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")

        if not os.path.exists(chunk_path) or os.path.getsize(chunk_path) <= 44:
            raise ValueError(f"Failed to create usable chunk {i}")

        chunks.append(chunk_path)

        print(
            f"Created chunk {i + 1}: "
            f"{len(chunk) / 1000:.2f} seconds"
        )

    if not chunks:
        raise ValueError("No audio chunks were generated.")

    print(f"Total chunks created: {len(chunks)}")
    return chunks


# 4. Main processing function
def process_input(input_source: str, is_youtube: bool = True):
    if not input_source:
        raise ValueError("Please provide an input source.")

    if is_youtube:
        audio_path = download_youtube_audio(input_source)
    else:
        audio_path = input_source

    wav_path = convert_to_wav(audio_path)
    chunks = chunk_audio(wav_path)

    print("Audio processing completed successfully.")
    return chunks
