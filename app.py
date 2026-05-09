from flask import Flask, jsonify
import os, time

app = Flask(__name__)
NODE_ID = os.environ.get("NODE_ID", "node-1")
START_TIME = time.time()

@app.route("/health")
def health():
    return jsonify({
        "node": NODE_ID,
        "status": "healthy",
        "uptime_seconds": round(time.time() - START_TIME, 1)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"[{NODE_ID}] Starting on port {port}")
    app.run(host="0.0.0.0", port=port)