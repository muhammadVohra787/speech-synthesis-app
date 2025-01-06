# Speech Synthesis App

This repository contains a web application that converts user-input text into speech using advanced text-to-speech (TTS) models. The app is built with [Streamlit](https://streamlit.io/), providing an interactive interface for users to generate and listen to synthesized speech.

## Features

- **Text Input**: Enter any text (up to 400 characters) to be converted into speech.
- **Speech Generation**: Utilizes pre-trained models to generate natural-sounding speech.
- **Audio Playback**: Listen to the generated speech directly within the app.
- **Volume Adjustment**: Automatically increases the volume of the generated speech for better clarity.

## Models and Libraries Used

- **[SpeechBrain's FastSpeech2](https://github.com/speechbrain/speechbrain)**: A fast and efficient model for text-to-speech conversion.
- **[SpeechBrain's HiFi-GAN](https://github.com/speechbrain/speechbrain)**: A high-fidelity generative adversarial network for audio generation.
- **[Streamlit](https://github.com/streamlit/streamlit)**: An open-source app framework for Machine Learning and Data Science projects.
- **[PyTorch](https://pytorch.org/)**: An open-source machine learning library for Python, used for deep learning applications.
- **[Torchaudio](https://pypi.org/project/torchaudio/)**: An audio library for PyTorch, providing easy access to common audio processing functions.
- **[Pydub](https://pypi.org/project/pydub/)**: A simple and easy high-level interface for audio manipulation.
- **[SciPy](https://scipy.org/)**: A Python library used for scientific and technical computing, here utilized for audio file handling.

## Installation

- **Clone the repository**:

  ```bash
  git clone https://github.com/yourusername/speech-synthesis-app.git
  cd speech-synthesis-app
  ```

- **Set up a virtual environment** (optional but recommended):

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

- **Install the required packages**:

  ```bash
  pip install -r requirements.txt
  ```

  Ensure that the `requirements.txt` file includes all necessary dependencies, such as:

  ```
  torch
  torchaudio
  streamlit
  scipy
  numpy
  pydub
  speechbrain
  ```

- **Install additional system dependencies**:

  - **FFmpeg**: Required by Pydub for audio processing.

    - **Ubuntu**:

      ```bash
      sudo apt update
      sudo apt install ffmpeg
      ```

    - **Windows**:

      Download and install FFmpeg from the [official website](https://ffmpeg.org/download.html).

## Usage

- **Run the Streamlit app**:

  ```bash
  streamlit run app.py
  ```

- **Access the app**:

  Open your web browser and navigate to `http://localhost:8501`.

- **Generate speech**:

  - Enter your desired text into the input box.
  - Click the "Generate Speech" button.
  - Wait for the processing to complete; a progress indicator will be displayed.
  - Once completed, the synthesized speech will be played automatically.

## Notes

- **Text Limit**: The input text is limited to 400 characters to ensure efficient processing.
- **Volume Adjustment**: The app increases the volume of the generated speech by 10 dB for better clarity.
- **Performance**: Processing time may vary depending on the length of the input text and system capabilities.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the developers of the models and libraries used in this project:

- [SpeechBrain](https://github.com/speechbrain/speechbrain)
- [Streamlit](https://github.com/streamlit/streamlit)
- [PyTorch](https://pytorch.org/)
- [Torchaudio](https://pypi.org/project/torchaudio/)
- [Pydub](https://pypi.org/project/pydub/)
- [SciPy](https://scipy.org/)

Feel free to explore and enhance the app to suit your needs!
``` 
