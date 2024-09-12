'''
Process audio input to determine sentiment and provide an audio response.
Please be calm, human.
'''

from threading import Thread, Event
import simpleaudio
import time

from mic_input import get_mic_input, close_mic
from speech_to_text import speech_to_text
from sentiment_analysis import get_sentiment_data

from globals import mic_data_queue
from globals import text_queue
from globals import sentiment_queue

NEGATIVITY_THRESHOLD = 100    # Threshold for triggering audio warning that you're negative
CONVERSION_FACTOR = 100       # Convert decimal sentiment (eg 0.64 -> 64)
SENTIMENT_DECAY = 1           # Reduction in sentiment per second

def main():

   thread_stop = Event()

   try:

      mic_thread =  Thread(target = get_mic_input, args = (thread_stop,))
      text_thread = Thread(target = speech_to_text)
      sentiment_thread = Thread(target = get_sentiment_data)

      mic_thread.start()
      text_thread.start()
      sentiment_thread.start()

      negativity_level = 0 # Baseline of zero "negativity"; higher number is more negative
      previous_time = time.time()

      while True:

         if not sentiment_queue.empty():

            sentiment_data = sentiment_queue.get()
            sentiment_analyser_result = sentiment_data['compound']
            print("Sentiment: ", sentiment_analyser_result)

            # Decay sentiment
            current_time = time.time()
            elapsed_time = current_time - previous_time
            previous_time = current_time
            negativity_level -= elapsed_time * SENTIMENT_DECAY

            # Update based on sentiment analysis
            sentiment_change = sentiment_analyser_result * -1 * CONVERSION_FACTOR
            negativity_level = max(0, negativity_level + sentiment_change)

            print("Current negativity level: ", negativity_level)

         if negativity_level > NEGATIVITY_THRESHOLD:
            print("CHILL OUT HUMAN !!!")

            clear_all_queues()

            thread_stop.set() # Pause mic_input thread
            wave_obj = simpleaudio.WaveObject.from_wave_file("tests/chill.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
            thread_stop.clear() # Continue mic_input thread

            negativity_level = NEGATIVITY_THRESHOLD


   except KeyboardInterrupt:
      print("\nProgram exiting...")
      thread_stop.set()
      close_mic()
      mic_thread.join(timeout = 1)
      text_thread.join(timeout = 1)


def clear_all_queues():

   while not mic_data_queue.empty():
      mic_data_queue.get()

   while not text_queue.empty():
      text_queue.get()

   while not sentiment_queue.empty():
      sentiment_queue.get()


if __name__ == '__main__':
    main()


'''
------------------------------------------------------------------------------------------------
TO DO NEXT
------------------------------------------------------------------------------------------------

x. Test everything is working ok
x. Look over the files for formatting, comments, etc
x. Put onto a Lego board for testing in kitchen
x. Make sure ReadMe is in a really good state
x. How to deploy properly as an application?

------------------------------------------------------------------------------------------------
PLAN
------------------------------------------------------------------------------------------------

Mic Input

Speech to Text

Sentiment Analysis

Speaker Output

   First stage: Single response
x. Record wav file for output when over threshold

   Next Stage: Text to speech processing
x. Develop sentences to output
x. Setup the good speech output service
x. Code the speaker_output to output text when triggered
x. At first, test with a single output.  Then can have this output vary based on severity

------------------------------------------------------------------------------------------------
THOUGHTS
------------------------------------------------------------------------------------------------

x. Add in joke api

'''
