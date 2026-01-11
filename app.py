from flask import Flask
from redis import Redis
import os, socket

app = Flask(__name__)
redis = Redis(host=os.environ.get("REDIS_HOST","redis"), port=int(os.environ.get("REDIS_PORT","6379")))

@app.route("/")
def index():
    count = redis.incr("hits")
    return f"Counter: {count} (served by {socket.gethostname()})"

@app.route("/health")
def health():
    try:
        redis.ping()
        return {"status":"healthy"}, 200
    except Exception as e:
        return {"status":"unhealthy","error":str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
