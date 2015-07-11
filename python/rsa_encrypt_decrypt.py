# coding: utf-8

"""加密算法：公钥(私钥)加密，私钥解密"""

from Crypto.PublicKey import RSA
from Crypto import Random

DATA = 'Hello, word!'
PRIVATE_KEY_PEM = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDB3c0nwVs6koPkpt6REeT07jK7m9qE9BmDw1Zl55T66rGfKM3g
1DFBq7jtcZ+xcgYAGgvJWPW16nylag/1lVNUxMShm2jlp3MwuBNKRvrXP2u29j9v
AAlM9lMLXzt0Ui4ZfLF9abpti5oD9tWy29Sp9Lt+0OWHKxp1QRazmykQeQIDAQAB
AoGAdL4FMcB9GFtscz+NXVyiPGBISrOCtndr+e2iVIFNNIAp8AcZWx9MfhhTpyC6
IpfgRyVoHZqldCO9Zbrl22RNpfybrP/2BeHx9xJWDXLXNAvDkZNCokCtc/bZYaQU
XCSYHUAmV078E0xZShwMwGu1YgZlz9er3XsqqBrT9ujDjIECQQDTOt+ukShtMJQd
6soNTA5+LU/kA+MKRB7oNPoviEMRRGeonD2ZXbjmzY6i1XJ/YsKPVuMkkvYCtPEY
KcvtCSApAkEA6vTMUBViRTr1Db63WBGpobAr9V8kiiMn6q2TuRBITsyijOgL6u+X
CrpRf+KDVyWC06ZHS/UFPPi+lubIgAU30QJAKtMp3HOTlaeer/4VHuMHoS9AnkLn
egJbncp32sEuj8almXqrxndI8IpGW98YipkURwlfnd+pvty+cJ6wuIr8GQJBAN/2
33cLGzSQ4ZzrigtqMr+Mlip8OfFvV5JtSR4kdjie+efFHe8h2WGBf0SfH8GHYTDt
FJNECW04Uzy22rKlxrECQQCtOkedu7SDr4tb3miKPNy5jyoVBRIR4QElE6DfZoDX
sxf4NowzBDwLbhYHNzSCl0xlIAA/xvFtRkEDtlYjq58n
-----END RSA PRIVATE KEY-----"""
PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDB3c0nwVs6koPkpt6REeT07jK7
m9qE9BmDw1Zl55T66rGfKM3g1DFBq7jtcZ+xcgYAGgvJWPW16nylag/1lVNUxMSh
m2jlp3MwuBNKRvrXP2u29j9vAAlM9lMLXzt0Ui4ZfLF9abpti5oD9tWy29Sp9Lt+
0OWHKxp1QRazmykQeQIDAQAB
-----END PUBLIC KEY-----"""


def _encrypt_by_public():
    random_func = Random.new().read
    public_key = RSA.importKey(PUBLIC_KEY_PEM)
    encrypted = public_key.encrypt(DATA, random_func)
    return encrypted


def _encrypt_by_private():
    random_func = Random.new().read
    private_key = RSA.importKey(PRIVATE_KEY_PEM)
    encrypted = private_key.encrypt(DATA, random_func)
    return encrypted


def _decrypt_by_private(msg_encrypt):
    private_key = RSA.importKey(PRIVATE_KEY_PEM)
    decrypted = private_key.decrypt(msg_encrypt)
    return decrypted


def _decrypt_by_public_err(msg_encrypt):
    """无效"""
    public_key = RSA.importKey(PUBLIC_KEY_PEM)
    decrypted = public_key.decrypt(msg_encrypt)
    return decrypted

if __name__ == '__main__':
    print(DATA, _decrypt_by_private(_encrypt_by_public()))
    print(DATA, _decrypt_by_private(_encrypt_by_private()))
    try:
        print(DATA, _decrypt_by_public_err(_encrypt_by_public()))
    except TypeError as e1:
        print(DATA, e1)
    try:
        print(DATA, _decrypt_by_public_err(_encrypt_by_private()))
    except TypeError as e2:
        print(DATA, e2)
