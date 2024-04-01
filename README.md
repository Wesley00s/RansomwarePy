# RansomwareTroll

**Description:**
RansomwareTroll is a simple ransomware project implemented in Python. It consists of two main scripts, `encrypter.py` and `decrypter.py`, which encrypt and decrypt files respectively using AES encryption.

**Legal Notice:**
This project is purely educational and should not be used for malicious purposes. The author is not responsible for any misuse of this software.

## Usage:

### Cryptography:
To encrypt a file, run `encrypter.py` with the file you want to encrypt as an argument.

```bash
python encrypter.py file_to_encrypt.txt
```

### Decryption:
To decrypt a file encrypted by RansomwareTroll, run `decrypter.py` with the encrypted file as an argument.

```bash
python decrypter.py crypto_file.txt.ransomwaretroll
```

## Requirements:
-Python 3.x
- `pyaes` library

You can install `pyaes` using pip:

```bash
pip install pyaes
```

## Files:

### `encrypter.py`:
This script encrypts a given file using AES encryption in CTR mode. It takes the file to be encrypted as input, encrypts it, and saves the encrypted data to a new file with the extension `.ransomwaretroll`. The original file is then deleted.

### `decrypter.py`:
This script decrypts a file encrypted by RansomwareTroll. It takes the encrypted file as input, decrypts it, and saves the decrypted data to a new file called `out.txt`. The encrypted file is then deleted.

### `out.txt`:
This file contains a warning about possible vulnerabilities related to the use of "jackson-dataformats-text" to parse TOML data, which could lead to Denial of Service (DoS) attacks.

## Security:
- The encryption key used in both scripts (`key=b"testsransomwares"`) is directly encoded for demonstration purposes. In a real-world scenario, a more secure method for generating and managing keys must be implemented.
- This ransomware uses AES encryption which is a strong encryption algorithm. However, the security of encryption depends on the strength of the key.

## Legal Notice:
This project is for educational purposes only. The author does not approve or support any illegal or malicious use of this software. Use it responsibly and ethically.