from secretpy import Playfair
from secretpy import CryptMachine
from secretpy.cmdecorators import NoSpaces, UpperCase


def encdec(machine, plaintext):
    print("Encrypting ... ")
    enc = machine.encrypt(plaintext)
    print("Encryption Done .... ")
    print("Writing Cipher.txt .... ")
    fout = open("Cipher.txt", "w")
    fout.write(enc)
    fout.close()
    print("Cipher.txt Ready")
    print("Decrypting .....")
    dec = machine.decrypt(enc)
    print("Decryption Completed")
    print("Creating Plaintext 2 .....")
    fout1 = open("Plaintext2.txt", "w")
    fout1.write(dec)
    fout1.close()
    print("Plaintext2 Ready")
    print("----------------------------------")
    return dec

def Pf_func():
    cm = NoSpaces(UpperCase(CryptMachine(Playfair())))
    alphabet = [
        u"0", u"1" , u"2",
        u"3",  u"4", u"5",
        u"6", u"7" , u"8",
    ]
    song = open('./src/example.wav', 'rb').read()
    plaintxt = open('.Plaintext.txt','w')
    cm.set_alphabet(alphabet)
    plaintext = ""
    for i in song:
        plaintext+=str(i)
    plaintxt.write(plaintext)
    plaintxt.close()
    res = encdec(cm, plaintext)
    res = list(map(int,res))
    xb = bytearray()
    for i in res:
        xb+=(i.to_bytes(4,"little"))
    print(xb)
    fout = open("./src/dec_pf.wav", "wb")
    fout.write(xb)
Pf_func()