'''
Create stream of audio data captured from mic
Convert audio data speech into text
'''

def get_mic_input():
  import speech_recognition as sr
  import os
  import json
  import pyaudio
  from vosk import Model, KaldiRecognizer

  vosk_model_path = "models/vosk-model-small-en-us-0.15"

  if not os.path.exists(vosk_model_path):
      print(f"Model not found at {vosk_model_path}")
      exit(1)

  model = Model(vosk_model_path)
  recogniser = KaldiRecognizer(model, 16000)

  audio_interface = pyaudio.PyAudio()
  stream = audio_interface.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
  stream.start_stream()

  print("Listening... Ctrl+C to stop.")

  try:
    while True:

      data = stream.read(4000, exception_on_overflow = False)

      if recogniser.AcceptWaveform(data):
        sentence_dict = json.loads(recogniser.Result())
        print(sentence_dict['text'])

  except KeyboardInterrupt:
    print("\nProgram interrupted with Ctrl+C. Exiting...")

  finally:
    stream.stop_stream()
    stream.close()
    audio_interface.terminate()
