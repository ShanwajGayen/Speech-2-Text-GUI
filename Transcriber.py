import speech_recognition as sr
from pydub import AudioSegment
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_audio_to_wav(input_path):
    audio = AudioSegment.from_file(input_path)
    wav_path = os.path.splitext(input_path)[0] + ".wav"
    audio.export(wav_path, format="wav")
    return wav_path

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    if not file_path.endswith(".wav"):
        file_path = convert_audio_to_wav(file_path)

    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Transcription for {os.path.basename(file_path)}:\n{text}\n")
        return text
    except sr.UnknownValueError:
        print(f"Could not understand: {file_path}")
    except sr.RequestError as e:
        print(f"❌ API error: {e}")

def transcribe_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Shorter noise calibration
        print("🎙️ Speak now...")
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=60)  # Faster capture
            text = recognizer.recognize_google(audio)
            print("📝 Transcription:", text)
        except sr.WaitTimeoutError:
            print("⚠️ Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("🤷 Could not understand audio.")
        except sr.RequestError as e:
            print(f"🚨 API error: {e}")
    

def select_file():
    file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        result = transcribe_audio(file_path)
        if result:
            messagebox.showinfo("Transcription", result)
        else:
            messagebox.showwarning("Transcription Failed", "Could not transcribe the selected file.")

def select_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if folder_path:
        for file in os.listdir(folder_path):
            if file.endswith(".mp3") or file.endswith(".wav"):
                transcribe_audio(os.path.join(folder_path, file))

# GUI Setup
root = tk.Tk()
root.title("🎧 Audio Transcriber")
root.geometry("300x200")

tk.Button(root, text="Transcribe Single File", command=select_file).pack(pady=10)
tk.Button(root, text="Batch Transcribe Folder", command=select_folder).pack(pady=10)
tk.Button(root, text="Transcribe from Microphone", command=transcribe_from_mic).pack(pady=10)

root.mainloop()