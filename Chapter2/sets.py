import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                decode_responses=True)


# Adding members into set
r.sadd('user:max:favoriteArtist', 'Arcade Fire', 'Arctic Monkeys',
       'Belle & Sebastian', 'Lenine')
r.sadd('user:hugo:favoriteArtist', "Daft Punk", "The Kooks",
       "Arctic Monkeys")

# finding values of set that intersect both given sets, returns a dict
print(r.sinter('user:max:favoriteArtist', 'user:hugo:favoriteArtist'))

# sdiff = elements of set1 that do not exist in set2
print(r.sdiff('user:max:favoriteArtist', 'user:hugo:favoriteArtist'))

print(r.sdiff('user:hugo:favoriteArtist', 'user:max:favoriteArtist'))

# sunion returns all elements f both sets
print(r.sunion('user:max:favoriteArtist', 'user:hugo:favoriteArtist'))

print(r.srandmember('user:max:favoriteArtist'))

print(r.srandmember('user:hugo:favoriteArtist'))

print(r.srem('user:max:favoriteArtist', 'Lenine'))
print(r.smembers('user:max:favoriteArtist'))


