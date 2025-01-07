import streamlit as st
from scipy.io.wavfile import write
import numpy as np
import io
from speechbrain.inference import HIFIGAN
from speechbrain.inference.TTS import FastSpeech2
from pydub import AudioSegment
from io import BytesIO
import time

# Cache model loading to avoid reloading on every button click
@st.cache_resource
def load_models():
    print("Loading models...")
    fastspeech2 = FastSpeech2.from_hparams(source="speechbrain/tts-fastspeech2-ljspeech", savedir="pretrained_models/tts-fastspeech2-ljspeech")
    hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="pretrained_models/tts-hifigan-ljspeech")
    print("Models loaded")
    return fastspeech2, hifi_gan

# Load models
fastspeech2, hifi_gan = load_models()

# Generate the speech from text
def text_to_speech(text:str, progress_bar:st.progress):
    print("Generating speech for: ", text[:10])
    progress_bar.progress(20)
    # Get the mel output and check its size
    mel_output, durations, pitch, energy = fastspeech2.encode_text(
        [text],
        pace=1.15,        # scale up/down the speed
        pitch_rate=1.0,  # scale up/down the pitch
        energy_rate=1.1, # scale up/down the energy
    )
    progress_bar.progress(40)
    notify_msg.write("Extracting Mel Spectrogram ... ")

    # Check the shape of the mel output
    print(f"Mel Output Shape: {mel_output.shape}")

    notify_msg.write("Extracting Waveforms ....")
    waveforms = hifi_gan.decode_batch(spectrogram=mel_output, hop_len=1)
    progress_bar.progress(70)
    return waveforms

# Set up Streamlit UI
st.title('Tacotron2 Text-to-Speech Web App')

# Text input with a maximum character limit
example_paragraphs = [
    "This is a sample paragraph for testing the text to speech functionality. You can copy and paste this text to see how the system works. The model should generate speech based on this input text.",
    "The rapid advancement of technology has led to significant changes in our daily lives. Innovations in communication, transportation, and entertainment have made the world more connected and accessible than ever before."
]

text_input = st.text_area(label='Enter Text for Speech:', help='Hello, welcome to the Streamlit TTS demo!', max_chars=400, value=example_paragraphs[0])

# Add a circular progress bar while generating speech
notify_msg = st.empty()

progress_bar = st.progress(0)
st.subheader("You can use one of these samples to test the model. Copy and paste the item into the input box and click generate speech")
for ex in example_paragraphs:
    st.write(ex)

if st.button('Generate Speech'):
    print(len(text_input))
    if text_input.strip() and len(text_input) > 6:
        notify_msg.write("Prasing text .... ")
        
        start = time.perf_counter()
        progress_bar.progress(10)
        
        # Generate waveform
        waveform = text_to_speech(text_input, progress_bar)
        progress_bar.progress(80)
        # Convert the waveform to 16-bit PCM format
        audio_data = waveform.squeeze().cpu().numpy()
        audio_data = (audio_data * 32767).astype(np.int16)

        # Save the audio as a temporary file
        audio_file = io.BytesIO()
        write(audio_file, 22050, audio_data)
        audio_file.seek(0)

        # Load the audio file using pydub
        audio = AudioSegment.from_wav(audio_file)

        # Increase the volume by 10 dB
        audio = audio + 10  # Adjust the value as needed

        # Export the modified audio to a BytesIO object
        audio_output = BytesIO()
        audio.export(audio_output, format='wav')
        audio_output.seek(0)

        # Play the audio in Streamlit
        st.audio(audio_output, format='audio/wav')

        end = time.perf_counter()
        elapsed = end - start
        print(f'Time taken: {elapsed:.6f} seconds')
        notify_msg.write("Done")
        # Update progress bar to 100% when done
        progress_bar.progress(100)

    else:
        st.error("Text needs to be over 5 characters")
