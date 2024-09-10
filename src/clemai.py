'''

'''

import mic_input

def main():

   # Todo: do we want to test the mic and speakers are working here?

    mic_input.get_mic_input()


    '''
    Threads

    1. mic_input_thread
       - continuous monitor for audio and add buffer to queue

    2. speech_to_text_thread

    3. sentiment_analysis_thread

    4. speech_output_thread

    '''

if __name__ == '__main__':
    main()


'''
NEXT

Mic Input

x. Try to get better performance from mic

---

Sentiment Analysis

x. Code the sentiment analyser
   - Download and run VADER

---

Speaker Output
x. Develop sentences to output
x. Setup the good speech output service
x. Code the speaker_output to output text when triggered

##################

THOUGHTS

x. Threading (see project doc)

x. Make sure we turn off audio input whilst playing from speaker

'''
