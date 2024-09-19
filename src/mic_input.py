'''
Create stream of audio data captured from mic.
'''

from globals import mic_data_queue

import pyaudio

stream = None
audio_interface = None

def get_mic_input(thread_stop):
  global stream, audio_interface
  audio_interface = pyaudio.PyAudio()
  stream = audio_interface.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
  stream.start_stream()

  print("Listening... Ctrl+C to stop.")

  while True:
    if not thread_stop.is_set():
        data = stream.read(8000, exception_on_overflow = False)
        mic_data_queue.put(data)


def close_mic():
    global stream, audio_interface
    if stream is not None:
        stream.stop_stream()
        stream.close()

    if audio_interface is not None:
        audio_interface.terminate()
