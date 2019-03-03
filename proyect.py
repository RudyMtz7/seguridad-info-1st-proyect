#ARC4
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto import Random
#DES
from Crypto.Cipher import DES3
#AES
from Crypto.Cipher import AES
#MD5
from Crypto.Hash import MD5
#SHA-1
from Crypto.Hash import SHA
#SHA-2
from Crypto.Hash import SHA256
#DSA
from Crypto.PublicKey import DSA
from Crypto.Random import random
#PSS
from Crypto.Signature import PKCS1_PSS
#RSA
from Crypto.PublicKey import RSA
from Crypto.Signature import DSS

import time
import hashlib

def main():
    #RC4
    countA = 0
    keysRC4 = [b'Very long and confidential key',b'Otro Mensaje raro',b'Otro Mensaje raro',b'Otro Mensaje raro',b'Otro Mensaje raro']
    for i in range(10000):
        if countA == 4:
            countA=0
        else:
            countA+= 1
        # print(keysRC4[count])
        function_arc4(keysRC4[countA])
    # rc4_file = open("test_vectors.txt", "r")
    # for line in rc4_file:
    #     print(line)
    #DES
    countB = 0
    keysDES = [b'Sixteen byte key',b'Sixteen byte key',b'Sixteen byte key',b'Sixteen byte key',b'Sixteen byte key']
    for i in range(10000):
        if countB == 4:
            countB=0
        else:
            countB+= 1
        # print(keysRC4[count])
        funtion_des(keysDES[countB])
    # des_file = open("des_vectors.txt", "r")
    # for line in des_file:
    #     print(line)
    # #AES
    countC = 0
    keysAES = [b'Sixteen byte key',b'Sixteen byte key',b'Sixteen byte key',b'Sixteen byte key',b'Sixteen byte key']
    for i in range(10000):
        if countC == 4:
            countC=0
        else:
            countC+= 1
        # print(keysRC4[count])
        funtion_aes(keysAES[countC])
    # function_dsa()
    function_dsa()
    # aes_file = open("aes_vectors.txt", "r")
    # for line in aes_file:
    #     print(line)
    # #Hash Vectors
    # hash_file = open("hash_vectors.txt", "r")
    # for line in hash_file:
    #     print(line)


#ARC4
def function_arc4(key):
    nonce = Random.new().read(16)
    tempkey = SHA.new(key+nonce).digest()
    cipher = ARC4.new(tempkey)
    msg = nonce + cipher.encrypt(b'Open the pod bay doors, HAL')
    # print(msg)

#DES
def funtion_des(key):
    iv = Random.new().read(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_OFB, iv)
    plaintext = b'sona si latine loqueris '
    msg = iv + cipher.encrypt(plaintext)
    # print(msg)

#AES
def funtion_aes(key):
    key = b'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')
    # print(msg)


def MD5():
    h = MD5.new()
    h.update(b'Hello')
    #print h.hexdigest()


def SHA_1():
    h = SHA.new()
    h.update(b'Hello')
    #print h.hexdigest()

def SHA_2():
    h = SHA256.new()
    h.update(b'Hello')
    # print h.hexdigest()

def function_rsa():
    message = '0000000000000000000000000000000000000000'
    key = RSA.construct(1024)
    h = SHA256.new(message)
    signature = pss.new(key).sign(h)
    verifier = pss.new(key)
    print(message)

def function_pss():
    message = 'To be signed'
    key = RSA.generate(2048)
    h = SHA.new()
    h.update(message.encode("utf8"))
    signer = PKCS1_PSS.new(key)
    # signature = PKCS1_PSS.sign(key)
    print(message)

def function_dsa():
    hash = hashlib.new('DSA')
    hash.update(b'Mensaje asdf')
    hash.digest()
    hash.hexdigest()
    print(hash)

main()
