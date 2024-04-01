import sys
import os
import pyaes

if len(sys.argv) < 2:
        print("Usage: python encrypter.py encrypted_file.txt.ransomwaretroll")
        sys.exit(1)

file_name = sys.argv[1]
file = open(file_name, "rb")
file_data = file.read()
file.close()


key = b"testsransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = "out.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()

