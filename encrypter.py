from cryptography import *
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('key.key', 'rb') as key:
    key = key.read()

choise: int = input("""
1) encrypte the files by the path
2) decrypte the files by the path
""")

def encryption():
    path = input("Enter the path: ")
    f = Fernet(key)

    with open(path, 'rb') as originale_file:
       originale = originale_file.read()
    
    encrypted = f.encrypt(originale)

    with open(path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decryption():
    path = input("Enter the path: ")
    f = Fernet(key)

    with open(path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

if choise == '1':
    encryption()
elif choise == '2':
    decryption()
    
