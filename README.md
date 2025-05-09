 Requirements
Python Packages (Install via pip):
sh
pip install SpeechRecognition pyttsx3 pyaudio
SpeechRecognition – For microphone input and speech-to-text (STT).

pyttsx3 – For text-to-speech (TTS) output.

pyaudio – Required for microphone access.

System Requirements
✔ Microphone (built-in or external)
✔ Internet Connection (for Google's speech recognition API)
✔ Python 3.6+

 Usage
Run the script:

sh
python speech_tts_assistant.py
Speak when prompted:

The program will say:

"Speech Recognition Active. Say 'exit' to quit."

Then, it will listen for your voice.

It will repeat what you say.

Say "exit" to quit.

 Overview
How It Works
Listens via Microphone:

Uses SpeechRecognition to capture audio.

Adjusts for background noise for better accuracy.

Converts Speech to Text:

Uses Google's free STT API (recognize_google()).

Speaks Back:

Uses pyttsx3 (offline TTS engine) to vocalize responses.
