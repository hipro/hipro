# -*- coding: utf-8 -*-

import json
from io import BytesIO

fp = BytesIO()

a = dict(a=10, b=100, c='applicable')
json.dump(a, fp)
fp.seek(0)
b = fp.read()
fp.close()

print(a)
print(b)
c = json.dumps(a)
print(c)
d = json.dumps(b)
print(d)
e = json.dumps(json.loads(b))
print(e)

"""
{'a': 10, 'c': 'applicable', 'b': 100}
{"a": 10, "c": "applicable", "b": 100}
{"a": 10, "c": "applicable", "b": 100}
"{\"a\": 10, \"c\": \"applicable\", \"b\": 100}"
{"a": 10, "c": "applicable", "b": 100}
"""
