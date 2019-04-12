import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                decode_responses=True)


def saveLink(id, author, title, link):
    r.hmset(name='link:' + str(id), mapping={"author": author,
                                             'title': title,
                                             'link': link})


def upVote(id):
    r.hincrby(name='link:' + str(id), key='score')


def downVote(id):
    r.hincrby(name='link:' + str(id), key='score', amount=-1)


# dont use hgetall for large records as it might slow down the redis database
# use hscan command
def showDetails(id):
    print(r.hgetall(name='link:' + str(id)))


saveLink(123, "dayvson", "Maxwell Dayvson's Github page",
         "https://github.com/dayvson")
upVote(123)
upVote(123)
saveLink(456, "hltbra", "Hugo Tavares's Github page",
         "https://github.com/hltbra")
upVote(456)
upVote(456)
downVote(456)

showDetails(123)
showDetails(456)
