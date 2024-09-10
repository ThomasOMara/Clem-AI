'''
Convert speech from mic into text stream
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
  #recogniser.SetWords(True) # For detailed jason
  word_array = []

  p = pyaudio.PyAudio()
  stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
  stream.start_stream()

  print("Listening... Ctrl+C to stop.")

  num_processed_words = 0

  try:
    while True:

      data = stream.read(4000, exception_on_overflow = False)

      '''
      if recognizer.AcceptWaveform(data):
        # Full result obtained after sentence completion
        result = json.loads(recognizer.Result())
        if 'text' in result and result['text'].strip():
          recognized_text = result['text']
          print(f"Recognized sentence: {recognized_text}")


      else:
        # Partial result obtained word by word
        partial_result = json.loads(recognizer.PartialResult())
        if 'partial' in partial_result and partial_result['partial'].strip():
          word = partial_result['partial']
          word_array.append(word)
          print(f"Recognized word: {word}")
      '''

      '''
      # Trying to get partial words (word-by-word)

      if recognizer.AcceptWaveform(data):
        sentence_dict = json.loads(recognizer.Result())
        results_sentence_len = len(sentence_dict['result'])
        for i in range(num_processed_words, results_sentence_len):
          word_array.append(sentence_dict['result'][i] )

        # Reset
        num_processed_words = 0
        sentence_dict = ""
        recognizer = KaldiRecognizer(model, 16000)
        recognizer.SetWords(True)

      else:

        partial_result = json.loads(recognizer.PartialResult())

        print(partial_result)
        #print(len(partial_result))

        if 'partial' in partial_result and partial_result['partial'].strip():
          word = partial_result['partial']

          print(partial_result)
          #print("word" + word)

          word_array.append(word)
          #print(f"Recognized word: {word}")
      '''

      # Just get the whole sentence

      if recogniser.AcceptWaveform(data):
        sentence_dict = json.loads(recogniser.Result())
        print(sentence_dict['text'])

        # Reset
        num_processed_words = 0
        sentence_dict = ""
        recogniser = KaldiRecognizer(model, 16000)
        #recogniser.SetWords(True)

  except KeyboardInterrupt:
    print("\nProgram interrupted with Ctrl+C. Exiting...")
    print(f"Captured words: {word_array}")

  finally:
    stream.stop_stream()
    stream.close()
    p.terminate()


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
