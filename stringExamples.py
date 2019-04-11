import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                encoding=u'utf-8',
                decode_responses=True)

# Multi-SET of keys
r.mset('first', "First Key Value", 'second', "Second key Value")

# Multi-Get
response = r.mget('first', 'second')
print(response)

