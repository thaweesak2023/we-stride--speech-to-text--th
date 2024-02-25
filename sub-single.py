# pip install moviepy speechrecognition pydub

import speech_recognition as sr
from moviepy.editor import VideoFileClip
import os

dir_out = 'out-txt-single'
if not os.path.exists(dir_out):
    os.makedirs(dir_out, exist_ok=True)


def video_to_text(video_path, audio_path='extracted_audio.wav', language="th-TH"):
    """Extracts audio from a video file, transcribes it to text, and saves the subtitles.

    Args:
        video_path (str): Path to the input video file.
        audio_path (str, optional): Path to save the extracted audio file. Defaults to 'extracted_audio.wav'.
        language (str, optional): Language code for speech recognition. Defaults to 'th-TH' (Thai).
    """

    # Extract audio from the video
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Transcribe the audio to text
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)

        try:
            text = r.recognize_google(audio_data, language=language)
            print(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")

    # Save the transcribed text as subtitles
    pathfile = f'{dir_out}/subtitles.txt'
    with open(pathfile, "w") as f:  # More generic filename
        f.write(text)


# Example usage:
my_video = 'Introducing_HTML_Tables.mp4'
video_to_text(my_video)
