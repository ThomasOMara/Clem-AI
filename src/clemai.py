'''

'''

import mic_input

def main():

    # Todo: do we want to test the mic and speakers are working here?

    mic_input.get_mic_input()

    '''
    while(True):
        print("hello world")

        # 1. Take input from mic and convert to text


        # 2. Run the sentiment analyser over the text input


        # 3. Output the set text via speaker

    '''

if __name__ == '__main__':
    main()


'''
NEXT

Mic Input

x. Try to get better performance from mic
x. Code mic_input to take input from mic
   - Maybe first save it down as a wav
x. Setup the google service to translate the audio to text
x. Link the mic_input to the google text api
   - Maybe first save down as a text file
---

Sentiment Analysis

x. Code the sentiment analyser
   - Develop list of words
   - Run over last x seconds of text
   - Test with actual speech to refine (look at transcripts)

---

Speaker Output
x. Develop sentences to output
x. Setup the good speech output service
x. Code the speaker_output to output text when triggered

##################

THOUGHTS

x. Do we need to download API keys or something?
   - How would be "hide" these from github - add to .gitignore?

x. We might want to create a new cpu thread for the audio input

x. Make sure we turn off audio input whilst playing from speaker

'''
