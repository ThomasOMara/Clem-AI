'''
Convert speech from mic to text

- PyAudio to interface with mic

- SpeechRecognition to listen to mic and convert the audio into text via
  Google Web Speech API

- Note: need to be able to read the speech word-for-word (ie not poll every
  second or something in case you miss words)

- Maybe can do every x seconds and remove duplicate words
  (want to include them though

'''

# I think you need to turn on port audio

# Then use pyaudio to create the stream

# Link this somehow to Google Web Speech API


import pyaudio
import wave

def get_mic_input():
  buffer_size = 1024
  audio_format = pyaudio.paInt16
  num_channels = 1
  sample_rate = 8000 # kHz sampling rate
  record_length = 5 # recording time in seconds
  output_filename = "output.wav"
  mic_device_index = 3

  pyaudio_instance = pyaudio.PyAudio()

  audio_input_stream = pyaudio_instance.open(
                      format = audio_format,
                      channels = num_channels,
                      rate = sample_rate,
                      input = True,
                      frames_per_buffer = buffer_size,
                      #input_device_index = mic_device_index
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
