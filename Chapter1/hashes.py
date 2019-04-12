import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                decode_responses=True)

r.hset(name='movie', key='title', value='The GodFather')

# r.hmset(name='movie', mapping={"title4": "The GodFather 2",
#                                "title2": "Back to the future",
#                                "title3": "Back to the future 2",
#                                "title3": "The shawshank redemption"})

# set a key of name 'movie' with the following fields
r.hmset(name='movie', mapping={'year': '1972',
                               'rating': '9.2',
                               'watchers': '1000000'})

print(r.hget(name='movie', key='title'))
print(r.hget(name='movie', key='rating'))

# increament the particular key of hash
r.hincrby(name='movie', key='watchers', amount=200)

# get a particular key of hash
print(r.hget(name='movie', key='watchers'))

# get all the fields of hash returns a dict
print(r.hgetall(name='movie'))

# only get keys returns a list
print(r.hkeys(name='movie'))
