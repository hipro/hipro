# coding: utf-8

# import uuid
import hmac
import hashlib
import time
from urlparse import urlsplit, parse_qs

APP_SECRET_DICT = {
    'f3d68088a37546b1adb468420538355c': 'c2460793785b43cda909677e0a69baa4'
}


def _hmac_sign(msg, secret):
    return hmac.new(msg, secret, hashlib.sha1).hexdigest()


def _verify(url):
    # <scheme>://<netloc>/<path>?<query>#<fragment>
    rlt = urlsplit(url)
    query_dict = parse_qs(rlt.query)
    timestamp = query_dict.get('timestamp', [''])[0]
    sign = query_dict.get('sign', [''])[0]
    app_id = query_dict.get('app_id', [''])[0]

    if not (timestamp and sign and app_id):
        return False
    try:
        timestamp = int(timestamp)
    except ValueError:
        return False
    if timestamp + 60 < int(time.time()):
        return False

    secret = APP_SECRET_DICT.get(app_id, '')
    return _hmac_sign(rlt.path + '?' + rlt.query[:rlt.query.index('&sign')], secret) == sign


def main():
    # secret = uuid.uuid4().hex
    app_id = 'f3d68088a37546b1adb468420538355c'
    secret = 'c2460793785b43cda909677e0a69baa4'
    item_id = 10
    timestamp = int(time.time())  # 1436802509
    uri_with_params = '/goods/get_qty?item_id=%s&timestamp=%s&app_id=%s' % (item_id, timestamp, app_id)
    sign = _hmac_sign(uri_with_params, secret)

    uri_with_sign = uri_with_params + '&sign=' + sign
    # print(secret, app_id, uri_with_params, sign, uri_with_sign)
    url = 'http://127.0.0.1' + uri_with_sign
    print(url)
    print(_verify(url))
    print(_verify('http://127.0.0.1'))
    time.sleep(61)
    print(_verify(url))


if __name__ == '__main__':
    main()
