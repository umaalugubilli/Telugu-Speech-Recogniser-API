import requests

url = "http://127.0.0.1:8000/recognize"
file_path = "/home/mahi/Documents/568/main_project/unknown_speakers_test/test3/seven.wav"

# Open the file in binary mode
with open(file_path, "rb") as file:
    files = {"file": file}
    response = requests.post(url, files=files)

# Print the response
print(response.json())
