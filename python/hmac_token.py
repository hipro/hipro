# coding: utf-8

"""
refer to
`https://github.com/zs1621/tornado-redis-session/blob/master/session.py`
`https://github.com/mmejia27/tornado-memcached-sessions/blob/master/session.py`
"""

import uuid
import hmac
import hashlib
import random
import string


def _generate_secret(length):
    return ''.join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits,
                                                                 string.punctuation)) for i in range(length)])


def _generate_id(secret):
    return hashlib.sha256(secret + str(uuid.uuid4())).hexdigest()


def _generate_hmac(session_id, secret):
    return hmac.new(session_id, secret, hashlib.sha256).hexdigest()


if __name__ == '__main__':
    secret = _generate_secret(64)
    session_id = _generate_id(secret)
    token = _generate_hmac(session_id, secret)
    print(secret, session_id, token)
    print(len(secret), len(session_id), len(token))
