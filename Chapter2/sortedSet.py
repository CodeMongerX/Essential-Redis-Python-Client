import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                decode_responses=True)

'''
A sorted set is different from set because of an associated score
and well.., its sorted
-> Not as fast as sets as scores are compared
-> speed of ops is O(Log(N)), where N is elements in set
-> implemented as two lists
    a) skip list with hash table
    b) Zip list
'''

r.zadd(name='Rajeev', mapping={'age': 23,
                               'occupation': 25})

resp = r.zrevrange("Rajeev", start=0, end=-1, withscores=True)
print(resp)
