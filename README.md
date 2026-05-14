# Distributed Health Monitor

A containerized multi-node health monitoring service demonstrating core concepts in distributed systems — node isolation, independent failure domains, and service observability.

## Motivation

In distributed systems, understanding node health is fundamental to fault tolerance. This project simulates a multi-node environment where each node exposes its own health status independently, reflecting real-world patterns used in systems like Kubernetes liveness probes and service mesh health checks.

## Architecture

Each node runs as an isolated Docker container, exposed on a different host port:

| Node   | Host Port | Endpoint                      |
|--------|-----------|-------------------------------|
| node-1 | 8081      | http://localhost:8081/health  |
| node-2 | 8082      | http://localhost:8082/health  |
| node-3 | 8083      | http://localhost:8083/health  |

Nodes share the same image but operate independently — failure in one does not affect others.

## Tech Stack

- Python (Flask) — lightweight HTTP service
- Docker — container runtime and image build
- Docker Compose — multi-node orchestration

## Quick Start

**Prerequisites:** Docker Desktop installed and running.

```bash
git clone https://github.com/YOUR_USERNAME/docker-demo.git
cd docker-demo
docker-compose up --build
```

Then query any node:

```bash
curl http://localhost:8081/health
curl http://localhost:8082/health
curl http://localhost:8083/health
```

## Example Response

```json
{
  "node": "node-1",
  "status": "healthy",
  "uptime_seconds": 42.3
}
```

## Concepts Demonstrated

- **Container isolation** — each node is an independent failure domain
- **Environment-based configuration** — node identity injected via environment variables, no hardcoding
- **Health endpoint pattern** — the `/health` route is standard in production systems (Kubernetes, AWS ELB, etc.)
- **Multi-service orchestration** — docker-compose manages networking and lifecycle of all nodes

## Background

This project was built as a hands-on introduction to container orchestration, alongside graduate research in distributed systems reliability and fault tolerance at Tokyo Metropolitan University.


## Kubernetes Deployment

The service can also be deployed to a Kubernetes cluster using the manifests in `k8s/`.

**Prerequisites:** minikube and kubectl installed.

```bash
# Start local cluster
minikube start

# Load image into minikube
minikube image load health-node:latest

# Deploy
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Verify pods are running
kubectl get pods

# Get access URL
minikube service health-node --url
```

### What Kubernetes adds over docker-compose

| Feature | docker-compose | Kubernetes |
|---|---|---|
| Multi-node | ✅ Manual config | ✅ Auto via replicas |
| Auto-restart | ❌ | ✅ Always restarts failed pods |
| Load balancing | ❌ | ✅ Service distributes traffic |
| Node identity | Manual env var | ✅ Auto from Pod metadata |