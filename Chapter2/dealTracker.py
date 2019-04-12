import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                decode_responses=True)


def markDealAsSent(dealId, userId):
    r.sadd(dealId, userId)


def sendDealIfNotSent(dealId, userId):
    reply = r.sismember(dealId, userId)
    if (reply):
        print("{dealId} was already sent to {userId}")
    else:
        print("sending")
        # code to send deal
        markDealAsSent(dealId, userId)


def showUsersThatReceivedAllDeals(dealIds):
    reply = r.sinter(dealIds)
    print(reply + " received all of the deals: " + dealIds)


def showUsersThatReceivedAtLeastOneOfTheDeals(dealIds):
    reply = r.sunion(dealIds)
    print(reply + " received at least one of the deals: " + dealIds)

markDealAsSent('deal:1', 'user:1')
markDealAsSent('deal:1', 'user:2')
markDealAsSent('deal:2', 'user:1')
markDealAsSent('deal:2', 'user:3')
sendDealIfNotSent('deal:1', 'user:1')
sendDealIfNotSent('deal:1', 'user:2')
sendDealIfNotSent('deal:1', 'user:3')
showUsersThatReceivedAllDeals("deal:1")
showUsersThatReceivedAtLeastOneOfTheDeals("deal:1")
