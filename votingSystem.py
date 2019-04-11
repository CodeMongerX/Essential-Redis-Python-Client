import redis

# init the redis obj
r = redis.Redis(host="127.0.0.1",
                port=6379,
                db=0,
                decode_responses=True)

# lets add some articles
r.set("article:12345:headline", "Google Wants to Turn Your Clothes into a "
      " Computer")
r.set("article:10001:headline", "For Millennials, the End of the TV Viewing "
      "Party")
r.set("article:60056:headline", "Alicia Vikander, Who Portrayed Denmark's "
      "Queen, Is Screen Royalty")


# upvoting method
def upVote(id):
    key = "article:" + str(id) + ":votes"
    r.incr(key)


# down voting
def downVote(id):
    key = "article:" + str(id) + ":votes"
    r.decr(key)


# Show results
def showResults(id):
    headlineKey = "article:" + str(id) + ":headline"
    voteKey = "article:" + str(id) + ":votes"
    response = r.mget(*(headlineKey, voteKey))
    print(response)


# driver code
upVote(12345)    # article:12345 has 1 vote
upVote(12345)    # article:12345 has 2 votes
upVote(12345)    # article:12345 has 3 votes
upVote(10001)    # article:10001 has 1 vote
upVote(10001)    # article:10001 has 2 votes
downVote(10001)  # article:10001 has 1 vote
upVote(60056)    # article:60056 has 1 vote

showResults(12345)
showResults(10001)
showResults(60056)
