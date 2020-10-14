import random

def encrypt(text,key):
	cipher=""
	for i in text:
		if i==' ':
			cipher+=' '
		else:
			cipher+=key[i]
	return cipher
 
def decrypt(cipher,key):
	pt=""
	def get_key(val,d): 
	    for key, value in d.items(): 
	         if val == value: 
	             return key
	for i in cipher:
		if i==' ':
			pt+=' '
		else:
			pt+=get_key(i,key)
	return pt
