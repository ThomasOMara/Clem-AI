# Clem-AI
Personal at-home serenity companion

## Features

## Installation

First install PortAudio then  PyAudio:
```bash
sudo apt-get install portaudio19-dev
sudo apt install python3-pyaudio
```

```bash
sudo apt-get install portaudio19-dev
sudo apt install python3-pyaudio
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
