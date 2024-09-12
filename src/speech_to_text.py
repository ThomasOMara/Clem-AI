'''
Convert mic data into text
'''

from globals import mic_data_queue
from globals import text_queue

import os
import json
from vosk import Model, KaldiRecognizer

def speech_to_text():

    vosk_model_path = "models/vosk-model-small-en-us-0.15"
    if not os.path.exists(vosk_model_path):
        print(f"Model not found at {vosk_model_path}")
        exit(1)

    model = Model(vosk_model_path)
    recogniser = KaldiRecognizer(model, 16000)

    while True:
        if not mic_data_queue.empty():
            data = mic_data_queue.get()
            if recogniser.AcceptWaveform(data):
                sentence_dict = json.loads(recogniser.Result())
                sentence_text = sentence_dict['text']
                print(sentence_text)
                text_queue.put(sentence_text)
