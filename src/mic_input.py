'''
Convert speech from mic into text stream
'''
def get_mic_input():
  import speech_recognition as sr
  import os
  import json
  from vosk import Model, KaldiRecognizer

  vosk_model_path = "models/vosk-model-small-en-us-0.15"

  if not os.path.exists(vosk_model_path):
      print(f"Model not found at {vosk_model_path}")
      exit(1)

  model = Model(vosk_model_path)
  recognizer = sr.Recognizer()

  with sr.Microphone() as source:

      print("Adjusting for ambient noise...")
      recognizer.adjust_for_ambient_noise(source)
      print("Say something:")
      audio = recognizer.listen(source)

      try:

          audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2) # Convert audio data into bytes for Vosk
          kaldi_recognizer = KaldiRecognizer(model, 16000) # Set up the Kaldi recognizer
          #kaldi_recognizer.SetWords(True)  # Enable detailed json output, including array of words

          if kaldi_recognizer.AcceptWaveform(audio_data):
              result = kaldi_recognizer.Result()
              result_json = json.loads(result)
              print("Recognized text:", result_json.get('text', ''))

          else:
              print("Could not understand the audio")

      except sr.UnknownValueError:
          print("Speech Recognition could not understand the audio")
      except sr.RequestError as e:
          print(f"Error with the Speech Recognition service: {e}")


'''
# Save mic input into wav file
def get_mic_input():

  import pyaudio
  import wave

  buffer_size = 1024
  audio_format = pyaudio.paInt16
  num_channels = 1
  sample_rate = 8000 # kHz sampling rate
  record_length = 5 # recording time in seconds
  output_filename = "output.wav"
  #mic_device_index = 3

  pyaudio_instance = pyaudio.PyAudio()

  audio_input_stream = pyaudio_instance.open(
                      format = audio_format,
                      channels = num_channels,
                      rate = sample_rate,
                      input = True,
                      frames_per_buffer = buffer_size,
                      #input_device_index = mic_device_index # Including throws error
                      )

  print("Recording in progress")

  stream_frames = []

  for _ in range(0, int(sample_rate / buffer_size * record_length)):
    data = audio_input_stream.read(buffer_size)
    stream_frames.append(data)

  print("Recording complete")

  audio_input_stream.stop_stream()
  audio_input_stream.close()
  pyaudio_instance.terminate()

  wave_file = wave.open(output_filename, 'wb')
  wave_file.setnchannels(num_channels)
  wave_file.setsampwidth(pyaudio_instance.get_sample_size(audio_format))
  wave_file.setframerate(sample_rate)
  wave_file.writeframes(b''.join(stream_frames))
  wave_file.close()
'''
