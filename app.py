import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def get_redis_client():
    try:
        return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, socket_connect_timeout=1)
    except Exception:
        return None

@app.route("/")
def index():
    try:
        r = get_redis_client()
        visits = r.incr("counter") if r else "Niedostępny"
    except Exception as e:
        visits = f"Brak połączenia z bazą ({str(e)})"

    return jsonify({
        "message": "Witaj w aplikacji demonstracyjnej DevOps!",
        "status": "success",
        "visits": visits,
        "environment": os.getenv("APP_ENV", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
