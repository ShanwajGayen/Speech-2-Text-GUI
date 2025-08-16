# Speech-2-Text-GUI
"Speech2Text-GUI is a Python-based tool that converts spoken audio into text using mic input or batch files. Featuring a user-friendly Tkinter interface, it supports real-time transcription, error handling, and output logging—ideal for productivity, accessibility, and documentation workflows.''

# 🎧 Audio Transcriber
A simple GUI-based tool to transcribe audio files and microphone input using Python's `speech_recognition` and `pydub`.
## Features
- Transcribe `.mp3` and `.wav` files
- Batch transcription from folders
- Live microphone input transcription
- GUI built with Tkinter
## Installation
```bash
pip install -r requirements.txt

## ⚙️ Usage
python transcriber.py

🔹 Requirements
- Python 3.x
- Libraries: speech_recognition, pyaudio, tkinter, os, datetime
🔹 Features
- 🎙️ Mic Input: Record and transcribe live speech
- 📁 Batch Mode: Transcribe multiple audio files at once
- 🧾 Output Logging: Save transcriptions with timestamps
- 🖥️ GUI Interface: Simple, menu-driven layout for ease of use
- 🛠️ Error Handling: Detects and reports missing files or mic issues
🔹 How to Run
python speech2text_gui.py
🔹 Workflow
- Launch the GUI
- Choose mic or batch mode
- Start recording or select audio files
- View and save transcriptions

