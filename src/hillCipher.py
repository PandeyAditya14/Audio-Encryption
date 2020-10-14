# Hill Cipher
from sympy.crypto.crypto import encipher_hill, decipher_hill
from sympy import Matrix
def hill_aud():
	with open("./src/example.wav", "rb") as f:
		x = f.read().hex()

	key = Matrix([[1, 1, 1, 2], [0, 1, 1, 0],
				  [2, 2, 3, 4], [1, 1, 0, 1]])

	# Encryption
	print("Encrypting .... ")
	ciphertext = ""
	for i in x:
		if i.isalpha():
			ciphertext+=encipher_hill(i,key)
		else:
			ciphertext+=i
	print("Completed Encrypting ..... ")
	with open("enc_hill.wav.crypt", "w") as f:
		f.write(ciphertext)

	print("Encrypted File Completed")
	print("Starting Decryption .... ")
	# Decryption
	pt = ""
	for i in ciphertext:
		if i.isalpha():
			pt+=decipher_hill(i,key)
		else:
			pt+=i

	with open("dec_hill.wav", "wb") as f:
		f.write(bytes().fromhex(pt))
	print("Completed Decryption")
	print("--------------------------------------------")