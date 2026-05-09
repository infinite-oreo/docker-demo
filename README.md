# Distributed Health Monitor

A containerized multi-node health monitoring service demonstrating core concepts in distributed systems — node isolation, independent failure domains, and service observability.

## Motivation

In distributed systems, understanding node health is fundamental to fault tolerance. This project simulates a multi-node environment where each node exposes its own health status independently, reflecting real-world patterns used in systems like Kubernetes liveness probes and service mesh health checks.

## Architecture
Client
├── GET localhost:8081/health  →  node-1 (container)
├── GET localhost:8082/health  →  node-2 (container)
└── GET localhost:8083/health  →  node-3 (container)


Each node runs as an isolated Docker container. Nodes share the same image but operate independently — failure in one does not affect others.

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
