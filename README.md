# Speaker Diarization Tool

## Overview

The **Speaker Diarization Tool** is a Streamlit application that allows users to upload a WAV audio file and splits it into segments based on individual speakers. This tool utilizes the [PyAnnote](https://github.com/pyannote/pyannote-audio) library for speaker diarization and [Pydub](https://github.com/jiaaro/pydub) for audio processing.

## Features

- Upload a WAV audio file.
- Process the audio to identify and split segments by speaker.
- Download a zip file containing the split audio segments.

## Prerequisites

To run this application, you'll need:

- Python 3.6 or higher
- An active Hugging Face account to obtain an authentication token for the PyAnnote model.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Astrasv/Speaker-diarization
   cd Speaker-diarization
   ```

2. Install the required packages:

   ```bash
   pip install streamlit pyannote.audio pydub
   ```

3. Create a file named `auth.py` in the same directory and add your Hugging Face authentication token:

   ```python
   auth_token = "your_hugging_face_auth_token"
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Upload a WAV audio file and click the "Split Audio by Speaker" button.

4. Wait for the processing to complete. Once finished, download the zip file containing the split audio segments.

## Code Explanation

- **split_audio_by_speaker**: This function performs speaker diarization on the uploaded audio file, splits the audio based on identified speaker segments, and saves them as individual WAV files in the specified output directory.
  
- **create_zip**: This function creates a zip file of the segmented audio files for easy downloading.

- **Streamlit UI**: The user interface is built using Streamlit, allowing users to upload files and initiate processing.

## Error Handling

The application includes error handling to manage issues related to loading the pipeline, audio file loading, and audio splitting.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [PyAnnote](https://github.com/pyannote/pyannote-audio)
- [Pydub](https://github.com/jiaaro/pydub)
