# Import redis package
import redis

# Create an redis object
r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                encoding=u'utf-8',
                decode_responses=True)

# Set the key and string
r.set("key", "Hello Redis!")

# Get the key back
response = r.get("key")
print(response)
