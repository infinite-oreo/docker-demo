"""
[INPUT]: 依赖环境变量 NODE_ID（节点身份）、PORT（监听端口）
[OUTPUT]: 对外提供 /health（查询状态）、/fail /recover（故障注入，POST）HTTP 端点
[POS]: 全项目唯一业务代码，被 Dockerfile 打包为镜像，docker-compose / k8s 以多副本方式启动同一份代码
[PROTOCOL]: 变更时更新此头部，然后检查上级 CLAUDE.md 是否需要同步
"""
from flask import Flask, jsonify
import os, time

app = Flask(__name__)
NODE_ID = os.environ.get("NODE_ID", "node-1")
START_TIME = time.time()
_healthy = True

@app.route("/health")
def health():
    body = {
        "node": NODE_ID,
        "status": "healthy" if _healthy else "unhealthy",
        "uptime_seconds": round(time.time() - START_TIME, 1)
    }
    return jsonify(body), 200 if _healthy else 503

@app.route("/fail", methods=["POST"])
def fail():
    global _healthy
    _healthy = False
    return jsonify({"node": NODE_ID, "status": "unhealthy"})

@app.route("/recover", methods=["POST"])
def recover():
    global _healthy
    _healthy = True
    return jsonify({"node": NODE_ID, "status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"[{NODE_ID}] Starting on port {port}")
    app.run(host="0.0.0.0", port=port)