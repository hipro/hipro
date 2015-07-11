# coding: utf-8
from Crypto.Cipher import AES

KEY = 'testtesttesttest'
DATA = '0123456789123456'


def main():
    aes = AES.new(KEY)
    encrypt_data = aes.encrypt(DATA)
    print(repr(encrypt_data))
    decrypt_data = aes.decrypt(encrypt_data)
    print(repr(decrypt_data))

if __name__ == '__main__':
    main()
