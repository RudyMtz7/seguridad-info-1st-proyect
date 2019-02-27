#ARC4
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto import Random
#DES
from Crypto.Cipher import DES3
from Crypto import Random
#AES
from Crypto.Cipher import AES
from Crypto import Random
#MD5
from Crypto.Hash import MD5
#SHA-1
from Crypto.Hash import SHA
#SHA-2
from Crypto.Hash import SHA256

def main():
    #RC4
    rc4_file = open("test_vectors.txt", "r")
    for line in rc4_file:
        print(line)
    #Hash Vectors
    hash_file = open("hash_vectors.txt", "r")
    for line in hash_file:
        print(line)

def ARC4(key):
    key = b'Very long and confidential key'
    nonce = Random.new().read(16)
    tempkey = SHA.new(key+nonce).digest()
    cipher = ARC4.new(tempkey)
    msg = nonce + cipher.encrypt(b'Open the pod bay doors, HAL')


def DES():
    key = b'Sixteen byte key'
    iv = Random.new().read(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_OFB, iv)
    plaintext = b'sona si latine loqueris '
    msg = iv + cipher.encrypt(plaintext)


def AES():
    key = b'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')



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

main()
