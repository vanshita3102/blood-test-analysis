# worker.py
import os
import redis
from rq import Worker, Queue

listen = ['default']
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    worker = Worker([Queue(name, connection=conn) for name in listen])
    worker.work()


