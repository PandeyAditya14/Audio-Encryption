from src import monoalpha
import random

def get_key():
	random.seed(123)

	list_ip = [chr(i) for i in range(65,91)]
	list_low = [chr(i) for i in range(97,123)]
	list_num = [i for i in range(0,10)]
	random.shuffle(list_ip)
	random.shuffle(list_low)
	random.shuffle(list_num)

	myd_up={}
	myd_low={}
	myd_num={}

	myd = {}
	ct_up = 65
	ct_low = 97
	for i in range(26):
		myd_up[chr(ct_up)]=list_ip[i]
		myd_low[chr(ct_low)]=list_low[i]
		if i < 10:
			myd_num[str(i)]=str(list_num[i])
		ct_up+=1
		ct_low+=1

	myd.update(myd_up)
	myd.update(myd_low)
	myd.update(myd_num)
	return myd

def mono_aud():
	print("Starting Monoalphabetic Cipher .. ")
	print("Creating Key .... ")
	key = get_key()
	print("Key Generated")
	print("Starting Encryption... ")
	with open("./src/example.wav", "rb") as f:
		fc = f.read()
	pt = fc.hex()

	ciphertext = monoalpha.encrypt(pt, key)

	with open("enc_mono.wav.monocrypt", "w") as f:
		f.write(ciphertext)
	print("Encryption Done")
	print("Decryption Starded .. ")
	with open("dec_mono.wav", "wb") as f:
		f.write(bytes().fromhex(monoalpha.decrypt(ciphertext, key)))
	print("Decryption Done File Save as dec_mono.wav")