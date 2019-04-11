import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                encoding=u'utf-8',
                decode_responses=True)

# # Multi-SET of keys
# r.mset('first', "First Key Value", 'second', "Second key Value")

# # Multi-Get
# response = r.mget('first', 'second')
# print(response)


'''
Traceback (most recent call last):
  File "stringExamples.py", line 10, in <module>
    r.mset('first', "First Key Value", 'second', "Second key Value")
TypeError: mset() takes 2 positional arguments but 5 were given
'''

# set so that it expires after 10 seconds
r.setex(name="ExpireKey", time=10, value="Boom!!!")

r.set(name="key", value="hello", ex=5, px=None, nx=True, xx=False)

