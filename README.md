# Clem-AI
Personal at-home serenity companion

## Features

### Mic Input

Constant audio input is recorded from the mic and converted into text using the Vosk speech-to-text model.

### Sentiment Analysis

The sentiment level (positive / negative) of the text is determined using the VADER sentiment analysis tool.

### AI Responses

Once the sentiment level is overly "negative", audio cues are provided for the humans to chill out and calm down.

## Installation

Note: On Debian systems, you may need to create and activate a virtual environment via venv.  If this is the case, then you may need to install pyaudio in the vm also.

```bash
python3 -m venv my_environ_name     # Create the virtual environment
source my_environ_name/bin/activate # Activate before use
deactivate                          # Deactivate when no longer needed
```

### Mic Input

Install PortAudio then PyAudio for mic input
```bash
sudo apt-get install portaudio19-dev
sudo apt install python3-pyaudio
```

Install Python speech recognition library
```bash
pip install SpeechRecognition
```

Install Vosk Speech Recognition module
```bash
pip3 install vosk
```

### Sentiment Analysis

Install VADER sentiment analysis module

Install Python speech recognition library
```bash
pip install vaderSentiment
```

## Usage

## Project Structure
- `clemai.py`: The main handler script responsible for calling the AI system and handling speech input / output.
- `audio_input.py`: Handles audio capture from the microphone and processes the data for analysis.
- `audio_output.py`: Responsible for playing back audio responses.
- `analyze_voice.py`: Contains the logic for analysing audio input, extracting features, and performing sentiment analysis.

## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Citations

### VADER

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
