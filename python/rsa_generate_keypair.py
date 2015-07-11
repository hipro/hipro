# coding: utf-8
from Crypto.PublicKey import RSA
from Crypto import Random

INPUT_SIZE = 1024


def main():
    random_func = Random.new().read
    key_pair = RSA.generate(INPUT_SIZE, random_func)
    private_pem = key_pair.exportKey()
    public_pem = key_pair.publickey().exportKey()
    print(private_pem)
    print(public_pem)


if __name__ == '__main__':
    main()