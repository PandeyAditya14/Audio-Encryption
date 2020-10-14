# Audio Encryption
## Introduction
This repository contains code for encrypting audio files using 
1. Hill Cipher
2. Monoalphabetic Cipher 
3. Playfair Cipher

## Methodology
To encrypt audio files(.wav) we read the files as raw bytes or more accurately binary numbers. These binary numbers are then 
converted into either Hexadecimal or Integer and then these Hexadecimals and Integers are used to encrypted and in all the
three algorithms our key is 0-9 in scrambled form or in case of hexadecimal \x00-\xFF
## Pre-Requisites

We use mainly use 2 crypto libraries:
1. [SecretPy](https://pypi.org/project/secretpy/)
2. [SymPy](https://www.sympy.org/en/index.html)

Both of these Libraries have to be installed separately before the usage of the program. To install these libraries use the commands
specified below. 
```bash
pip install secretpy
pip install sympy
```

## Usage
You just need to execute the main.py as it is the wrapper program that abstracts complexities from the user. To run the wrapper
program execute the follow in command in the project folder.
```bash
python3 main.py
```
Or simply run the main.py if you are on windows

## File Structure
* [/src](./src)  Contains the The code for the all three cryptographic algorithms and the related file
* The decrypted audio is shown in the root folder project along with the source audio and thus can be matched with source audio by the user to see
if the process was successful.

## Important Points
* Playfair Cipher may result in an empty audio files in some cases in these cases Plaintext2.txt can be matched with Plaintext.txt as it is the 
decrypted form of Plaintext.txt and both are binary dumps of the audio file.
* Hill Cipher may take a really long time for completion of deciphering the audio as it has to calculate inverse of a matrix for every 4 bits and the audio file is 241 KB.

## License
[MIT](https://choosealicense.com/licenses/mit/)