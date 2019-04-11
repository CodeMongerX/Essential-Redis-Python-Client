import redis

# init the redis obj
r = redis.Redis(host="127.0.0.1",
                port=6379,
                db=0,
                decode_responses=True)


# add some elements into the list
r.lpush("books", *("clean code", "Code Complete", "Peopleware"))


# get item at index
print(r.lindex("books", 2))


# Get the length of the list
respllen = r.llen(name="books")
print("length of list books is ", r.llen("books"))


# Get a subset of the list items including start & end
# index starts at 0
# even if index is out of bound, returns till last element.
# Can also use negitive numbers, same like python slicing
resplrange = r.lrange(name="books", start=0, end=-2)
print(resplrange)


# LPOP returns first element while RPOP returns last element
print(r.lpop(name='books'))
print(r.rpop(name='books'))


r.flushdb()
