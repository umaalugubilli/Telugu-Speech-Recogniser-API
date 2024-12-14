from fastapi import FastAPI, UploadFile, File
from model.prediction import Keyword_Spotting_Service
import os

app = FastAPI()

# Instantiate the Keyword Spotting Service singleton
kss = Keyword_Spotting_Service()

@app.post("/recognize")
async def recognize_digit(file: UploadFile = File(...)):
    """
    Endpoint to predict the digit from the uploaded audio file.

    :param file: Uploaded .wav file
    :return: Predicted digit
    """
    # Step 1: Read the uploaded file
    audio_data = await file.read()

    # Step 2: Save the audio file temporarily (needed for librosa to process it)
    temp_file_path = "temp_audio.wav"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(audio_data)

    # Step 3: Use the Keyword Spotting Service to predict the digit
    predicted_digit = kss.predict(temp_file_path)

    os.remove(temp_file_path)

    return {"predicted_digit": predicted_digit}
