import sounddevice as sd
import numpy as np
import queue
import threading
import soundfile as sf
import datetime
from pynput import keyboard

# Globale Variablen
SAMPLING_RATE = 44100
BUFFER_DURATION = 0.6  # 0.1 Sekunden vor und 1 Sekunde nach dem Drücken
buffer_size = int(BUFFER_DURATION * SAMPLING_RATE)
audio_buffer = np.zeros((buffer_size, 2), dtype=np.float32)
audio_queue = queue.Queue()

# Funktion, um kontinuierlich Audio aufzunehmen
def audio_callback(indata, frames, time, status):
    global audio_buffer
    audio_buffer = np.roll(audio_buffer, -frames, axis=0)
    audio_buffer[-frames:, :] = indata

# Starten der kontinuierlichen Aufnahme
stream = sd.InputStream(callback=audio_callback, channels=2, samplerate=SAMPLING_RATE)
stream.start()

# Funktion zum Speichern der Audiodaten
def save_audio():
    while True:
        item = audio_queue.get()
        if item is None:
            break  # Beenden, wenn None als Signal zum Beenden empfangen wird
        audio_data, key_name = item
        filename = f"./Data/{key_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"
        sf.write(filename, audio_data, SAMPLING_RATE)
        print(f"Audio saved as {filename}")

# Funktion, um auf Tastendruck zu reagieren
def on_press(key):
    try:
        key_name = key.char  # Versuche, das Zeichen der Taste zu erhalten
    except AttributeError:
        key_name = key.name  # Wenn es kein Zeichen gibt, verwende den Namen der Taste

    current_buffer = np.copy(audio_buffer)a
    audio_queue.put((current_buffer, key_name))

    if key == keyboard.Key.esc:
        # Beenden, wenn die Escape-Taste gedrückt wird
        return False

# Listener für Tastatureingaben
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Starten des Speicher-Threads
save_thread = threading.Thread(target=save_audio)
save_thread.start()

# Warte, bis der Listener beendet wird (durch Drücken der Escape-Taste)
listener.join()

# Signal zum Beenden an den Speicher-Thread senden und warten
audio_queue.put(None)
save_thread.join()