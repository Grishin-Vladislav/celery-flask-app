import requests
from base64 import b64encode

base_url = "http://127.0.0.1:5000/upscale"

with open('../upscaler/lama_300px.png', 'rb') as file:
    encoded_file = b64encode(file.read())
    print(encoded_file)
    rsp = requests.post(base_url,
                        files={file.name: encoded_file})

print(rsp.status_code)
print(rsp.text)
