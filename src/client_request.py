import requests

url = "http://127.0.0.1:8000/recognize"
file_path = "test/test_audio_files/test3/zero.wav"

# Open the file in binary mode
with open(file_path, "rb") as file:
    files = {"file": file}
    response = requests.post(url, files=files)

# Print the response
print(response.json())
