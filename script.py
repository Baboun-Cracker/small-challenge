import pickle
from hashlib import sha512

with open('hash', 'rb') as f:
    unpickler = pickle.Unpickler(f)
    password = unpickler.load()


def caesar(password):
    for i in range(1):
        key = sha512(password.encode('utf-8')).digest()
        with open("files", 'rb') as f_entree:
            with open(final_file, 'wb') as f_sortie:
                i = 0
                while f_entree.peek():
                    f_sortie.write(bytes([ord(f_entree.read(1))^key[i % len(key)]]))
                    i += 1


input_password = input("Enter the password for decrypt the files : ")

if sha512(input_password.encode()).digest() == password:
    final_file = input("Enter the name of final file : ")
    caesar(input_password)

else:
    print(f"'{input_password}' is not the correct password")