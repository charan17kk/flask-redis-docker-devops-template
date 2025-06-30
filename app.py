from flask import Flask
import redis
import os  

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379)
# talks to the redis container

@app.route('/')
def hello():
    count = r.incr('hits')  # increments the 'hits' counter
    return f'Hello! This page has been viewed {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # binds to all interfaces
