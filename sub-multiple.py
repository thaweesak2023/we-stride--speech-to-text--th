# pip install moviepy speechrecognition pydub

from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr


dir_out = 'chunks'
dir_temp = 'temps'


def video_to_subtitles(video_path, language='th-TH', min_silence_len=500, silence_thresh=-40):
    # Extract audio from video
    video = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)

    # Load and split audio
    audio = AudioSegment.from_wav(audio_path)
    chunks = split_on_silence(
        audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    r = sr.Recognizer()

    subtitles = []
    start_time = 0

    for i, chunk in enumerate(chunks):
        # Calculate chunk duration
        chunk_duration = len(chunk) / 1000.0

        # Export chunk to a wav file
        chunk_path = f"{dir_temp}/temp_chunk{i}.wav"
        chunk.export(chunk_path, format="wav")

        with sr.AudioFile(chunk_path) as source:
            audio_data = r.record(source)
            try:
                text = r.recognize_google(audio_data, language=language)
                end_time = start_time + chunk_duration
                subtitles.append(
                    {'start': start_time, 'end': end_time, 'text': text})
            except sr.UnknownValueError:
                print(f"Chunk {i}: Could not understand audio")
            except sr.RequestError as e:
                print(f"Chunk {i}: Could not request results; {e}")

        start_time += chunk_duration

    # Generate SRT file
    with open("output_subtitles.srt", "w") as f:
        for i, subtitle in enumerate(subtitles, start=1):
            start = format_srt_time(subtitle['start'])
            end = format_srt_time(subtitle['end'])
            f.write(f"{i}\n{start} --> {end}\n{subtitle['text']}\n\n")


def format_srt_time(seconds):
    """Convert seconds to SRT time format."""
    ms = int((seconds % 1) * 1000)
    s = int(seconds)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


# Example usage:
video_path = "Introducing_HTML_Tables.mp4"
video_to_subtitles(video_path)
