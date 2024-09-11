'''
Process audio input to determine sentiment and provide an audio response
Please be calm, human
'''

from threading import Thread, Event
from mic_input import get_mic_input, close_mic
from speech_to_text import speech_to_text

def main():

   thread_stop = Event()

   try:
      mic_thread =  Thread(target = get_mic_input, args = (thread_stop,))
      text_thread = Thread(target = speech_to_text, args = (thread_stop,))

      mic_thread.start()
      text_thread.start()

   except KeyboardInterrupt:
      print("\nProgram exiting...")
      thread_stop.set()
      close_mic()
      mic_thread.join(timeout = 1)
      text_thread.join(timeout = 1)

   '''
   Threads

   1. mic_input_thread
      - continuous monitor for audio and add buffer to mic_input_queue
      - signals speech_to_text_thread when item added to mic_input_queue

   2. speech_to_text_thread
      - when item added to mic_input_queue, wakes and processes text
      - add text to text_queue
      - signals sentiment_analysis_thread

   3. sentiment_analysis_thread

   4. speech_output_thread

   '''

if __name__ == '__main__':
    main()


'''
NEXT

Threading

x. Implement the current functionality with a thread
x. Break out mic-input and speech-to-text as threads
x. Add mic data to queue
   - Speech to text thread needs to wait for signal (items in mix_queue)
   - Mutex lock on mic_queue when updated (adding / removing)
x. Code up sentiment analyser as thread
   - Sentiment analyser needs to wait for signal (items in text_queue)
   - Mutex lock on text_queue when updated (adding / removing)

---

Mic Input


Speech to Text
x. Seperate into another file


Sentiment Analysis
x. VADER -> run over de-queued text
x. Have sentiment_analysis just return the data.  clemai handles the logic

   clemai.py
x. Perhaps have a number that moves up and down as new sentiment arrives?
x. Sentiment level will decrease natually over time and if positive sentences returned

Speaker Output
x. Develop sentences to output
x. Setup the good speech output service
x. Code the speaker_output to output text when triggered
x. At first, test with a single output.  Then can have this output vary based on severity

##################

THOUGHTS

x. Threading (see project doc)

x. Make sure we turn off audio input whilst playing from speaker

x. Add in joke api

'''
