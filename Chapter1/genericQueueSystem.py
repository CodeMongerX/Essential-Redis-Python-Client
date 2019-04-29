import redis

# Redis object
r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                decode_responses=True)


class Queue:

    def __init__(self, queueName, redisClient):
        self.queueName = queueName
        self.redisClient = redisClient
        self.queueKey = 'queues:' + queueName
        self.timeOut = 0  # zero means no timeout

    def size(self):
        self.redisClient.llen(self.queueKey)

    def push(self, queueName, data):
        self.redisClient.lpush(self.queueName, data)

    def pop(self):
        self.redisClient.brpop(self.queueKey, self.timeOut)

logsQueue = Queue(queueName="logs", redisClient=r)
max = 5
for i in range(max):
    logsQueue.push("logs", "HelloWorld" + str(i))
print("Created {} logs".format(max))

for i in range(max):
    print(logsQueue.pop())
    print(logsQueue.size() + " logs left")
