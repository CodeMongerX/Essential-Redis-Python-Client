import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                encoding=u'utf-8',
                decode_responses=True)

# Multi-SET of keys: use dict for all these
r.mset({'first': 'FirstKeyValue', 'second': 'SecondkeyValue'})

# Multi-Get
response = r.mget(*('first', 'second'))
print("MSET & MGET: ", end="")
print(response)


# set so that it expires after 10 seconds
r.setex(name="ExpireKey", time=10, value="Boom!!!")

r.set(name="key", value="hello", ex=5, px=None, nx=True, xx=False)
