import speech_recognition as sr
import keyboard
import pyaudio
import wave
from colorama import *
import time


def speech_to_text():
    audio = record_audio()
    text = transcribe_audio(audio)
    return text


# function to get the user's input audio
def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "input.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    # print("Recording...")
    print("\rYou " + Fore.RED + Style.BRIGHT +  "[Recording]"  + Fore.RESET + ": ", end="", flush=True)

    while keyboard.is_pressed('RIGHT_SHIFT'):
        data = stream.read(CHUNK)
        frames.append(data)
    # print("Stopped recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return WAVE_OUTPUT_FILENAME

def transcribe_audio(file_audio):
    r = sr.Recognizer()
    with sr.AudioFile(file_audio) as source:
            audio = r.record(source)  # read the entire audio file                  
            try:
                result = r.recognize_google(audio, language="id-ID")
                # print("Transcription: " + result)
                return result
            except:
                # print("can u repeat?")
                return ""
