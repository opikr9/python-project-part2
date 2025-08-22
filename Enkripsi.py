import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"karakter: {chars}")
# print(f"kunci: {key}")

# enkripsi
text_input = input("Masukan pesan untuk di enkripsi: ")
cipher_text = ""

for letter in text_input:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Text normal: {text_input}")
print(f"Text enkripsi: {cipher_text}")

# dekripsi
cipher_text = input("Masukan pesan untuk di dekripsi: ")
text_input = ""

for letter in cipher_text:
    index = key.index(letter)
    text_input += chars[index]

print(f"Text enkripsi: {cipher_text}")
print(f"Text normal: {text_input}")