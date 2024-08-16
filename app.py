import streamlit as st
from pyannote.audio import Pipeline
from pydub import AudioSegment
import os
import zipfile

def split_audio_by_speaker(input_audio_path, output_dir, auth_token):
    try:
        pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=auth_token)
    except Exception as e:
        return f"Error loading the pipeline: {e}"

    try:
        diarization = pipeline(input_audio_path)
    except Exception as e:
        return f"Error during diarization: {e}"

    try:
        audio = AudioSegment.from_wav(input_audio_path)
    except Exception as e:
        return f"Error loading audio file: {e}"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_paths = []
    try:
        for i, (turn, _, speaker) in enumerate(diarization.itertracks(yield_label=True)):
            start_ms = int(turn.start * 1000)
            end_ms = int(turn.end * 1000)
            speaker_audio = audio[start_ms:end_ms]

            output_path = os.path.join(output_dir, f"speaker_{speaker}_{i}.wav")
            speaker_audio.export(output_path, format="wav")
            output_paths.append(output_path)

        return output_paths

    except Exception as e:
        return f"Error during audio splitting: {e}"

def create_zip(output_dir):
    zip_filename = "speaker_segments.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(output_dir):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                zipf.write(filepath, os.path.relpath(filepath, output_dir))
    return zip_filename

# Streamlit UI
st.title("Speaker Diarization Tool")
st.info("Upload an audio file and get segments split by speaker.")

# File uploader
uploaded_file = st.file_uploader("Choose a WAV audio file", type="wav")

if st.button("Split Audio by Speaker"):
    if uploaded_file is not None:
        input_audio_path = "uploaded_audio.wav"
        with open(input_audio_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        output_dir = "speaker_segments"
        
        auth_token = st.secrets["auth"]["token"]
        
        with st.spinner("Processing..."):
            result = split_audio_by_speaker(input_audio_path, output_dir, auth_token)

            if isinstance(result, list):
                st.success("Audio split successfully!")
                
                zip_file_path = create_zip(output_dir)
                
                with open(zip_file_path, "rb") as f:
                    st.download_button("Download Zip File", f, file_name=zip_file_path)

            else:
                st.error(result)
    else:
        st.error("Please upload a WAV file.")
