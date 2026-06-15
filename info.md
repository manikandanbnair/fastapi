# Docker Learning Cheat Sheet

# Core Mental Model

```text
Dockerfile
    ↓
Docker Build
    ↓
Docker Image
    ↓
Docker Run
    ↓
Container
```

---

# Images vs Containers

Image:

* Blueprint
* Read-only template
* Used to create containers

Container:

* Running instance of an image
* Has its own process, network, filesystem

Example:

```text
Image: fastapi-backend:latest
        ↓
Container 1
Container 2
Container 3
```

---

# Build vs Deploy

Build:

```bash
docker build -t fastapi-backend .
```

Creates an image.

Deploy:

```bash
docker run fastapi-backend
```

Creates a container from the image.

---

# Docker Images

## List Images

```bash
docker images
```

## Build Image

```bash
docker build -t fastapi-backend .
```

## Build with Version Tag

```bash
docker build -t fastapi-backend:v1 .
```

## Remove Image

```bash
docker rmi IMAGE_ID
```

---

# Docker Containers

## Run Container

```bash
docker run fastapi-backend
```

## Run Detached

```bash
docker run -d fastapi-backend
```

## Run with Port Mapping

```bash
docker run -p 8000:8000 fastapi-backend
```

Request Flow:

```text
Browser
    ↓
localhost:8000
    ↓
Container Port 8000
```

## List Running Containers

```bash
docker ps
```

## List All Containers

```bash
docker ps -a
```

## Stop Container

```bash
docker stop CONTAINER_ID
```

## Start Container

```bash
docker start CONTAINER_ID
```

## Restart Container

```bash
docker restart CONTAINER_ID
```

## Remove Container

```bash
docker rm CONTAINER_ID
```

---

# Container Logs

## View Logs

```bash
docker logs CONTAINER_ID
```

## Follow Logs

```bash
docker logs -f CONTAINER_ID
```

---

# Execute Commands Inside Container

## Open Shell

```bash
docker exec -it CONTAINER_ID bash
```

or

```bash
docker exec -it CONTAINER_ID sh
```

---

# Dockerfile

## Typical Flow

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build:

```bash
docker build -t fastapi-backend .
```

Run:

```bash
docker run -p 8000:8000 fastapi-backend
```

---

# Docker Networking

## Port Mapping

```bash
docker run -p 8000:8000 fastapi-backend
```

Meaning:

```text
Host Port      Container Port
8000     →     8000
```

Access:

```text
http://localhost:8000
```

---

# Docker Compose

## Start Services

```bash
docker compose up
```

## Detached Mode

```bash
docker compose up -d
```

## Stop Services

```bash
docker compose down
```

## View Containers

```bash
docker compose ps
```

## View Logs

```bash
docker compose logs
```

## Follow Logs

```bash
docker compose logs -f
```

## Rebuild Images

```bash
docker compose up --build
```

---

# FastAPI + PostgreSQL Compose Model

```text
FastAPI Container
        ↓
Docker Network
        ↓
PostgreSQL Container
```

Compose automatically creates:

* Network
* Container communication
* Startup orchestration

---

# Docker Hub

## Login

```bash
docker login
```

## Tag Image

```bash
docker tag fastapi-backend manikandanbnair/fastapi-backend:v1
```

## Push Image

```bash
docker push manikandanbnair/fastapi-backend:v1
```

## Pull Image

```bash
docker pull manikandanbnair/fastapi-backend:v1
```

---

# Registry Workflow

```text
Developer
    ↓
docker build
    ↓
Image
    ↓
docker push
    ↓
Docker Hub
```

Another Machine:

```text
docker pull
    ↓
Image
    ↓
docker run
    ↓
Container
```

---

# Jenkins + Docker

Build Stage:

```bash
docker build -t fastapi-backend .
```

Deploy Stage:

```bash
docker compose up -d
```

Production Pattern:

```text
Build Once
    ↓
Push Once
    ↓
Deploy Many Times
```

---

# Common Troubleshooting

## Check Running Containers

```bash
docker ps
```

## Check Logs

```bash
docker logs CONTAINER_ID
```

## Inspect Container

```bash
docker inspect CONTAINER_ID
```

## Enter Container

```bash
docker exec -it CONTAINER_ID bash
```

---

# Concepts Learned

## Image

Blueprint for containers.

## Container

Running instance of an image.

## Dockerfile

Instructions to build an image.

## Docker Compose

Defines and runs multi-container applications.

## Registry

Stores images.

Examples:

* Docker Hub
* ECR
* GCR
* ACR

## Build Once, Deploy Many Times

```text
Code
 ↓
Image
 ↓
Registry
 ↓
Multiple Deployments
```

Never rebuild for every environment.



# Kubernetes Learning Cheat Sheet (Current Progress)

## Mental Model

```text
Deployment
    ↓
ReplicaSet
    ↓
Pods
    ↓
Containers
```

```text
Service
    ↓
Finds Pods using Labels
    ↓
Load Balances Traffic
```

---

# Cluster Information

## Check Cluster

```bash
kubectl cluster-info
```

## Check Nodes

```bash
kubectl get nodes
```

## Detailed Node Information

```bash
kubectl get nodes -o wide
```

---

# Deployments

## List Deployments

```bash
kubectl get deployments
```

## Create/Update Deployment

```bash
kubectl apply -f deployment.yaml
```

## Delete Deployment

```bash
kubectl delete deployment fastapi-deployment
```

## Scale Deployment

```bash
kubectl scale deployment fastapi-deployment --replicas=3
```

## Deployment Details

```bash
kubectl describe deployment fastapi-deployment
```

---

# ReplicaSets

## List ReplicaSets

```bash
kubectl get rs
```

## ReplicaSet Details

```bash
kubectl describe rs <replicaset-name>
```

Example:

```bash
kubectl describe rs fastapi-deployment-788948bb5d
```

---

# Pods

## List Pods

```bash
kubectl get pods
```

## List Pods with More Information

```bash
kubectl get pods -o wide
```

## Watch Pods Live

```bash
kubectl get pods -w
```

## Pod Details

```bash
kubectl describe pod <pod-name>
```

## View Logs

```bash
kubectl logs <pod-name>
```

## Delete Pod

```bash
kubectl delete pod <pod-name>
```

---

# Services

## List Services

```bash
kubectl get svc
```

## Service Details

```bash
kubectl describe svc fastapi-service
```

## Create/Update Service

```bash
kubectl apply -f service.yaml
```

---

# Port Forwarding

## Forward Service Port

```bash
kubectl port-forward service/fastapi-service 8000:8000
```

Access:

```text
http://localhost:8000/docs
```

## Forward Pod Port

```bash
kubectl port-forward pod/<pod-name> 8000:8000
```

---

# Endpoints

## View Endpoints

```bash
kubectl get endpoints
```

Example:

```text
NAME              ENDPOINTS
fastapi-service   10.244.0.5:8000
```

---

# YAML Apply Workflow

## Create or Update Resources

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## Delete Resources

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

---

# Troubleshooting Flow

When something is broken:

```text
Deployment
    ↓
Pods
    ↓
Describe Pod
    ↓
Logs
    ↓
Find Root Cause
```

Commands:

```bash
kubectl get deployments
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

---

# Scaling

Current:

```yaml
replicas: 1
```

Scale to:

```yaml
replicas: 3
```

or

```bash
kubectl scale deployment fastapi-deployment --replicas=3
```

What happens:

```text
Deployment
    ↓
ReplicaSet
    ↓
Creates More Pods
```

Service remains unchanged.

---

# Labels and Selectors

Deployment Labels:

```yaml
labels:
  app: fastapi
```

Service Selector:

```yaml
selector:
  app: fastapi
```

Service finds Pods using matching labels.

---

# Service Types Learned

## ClusterIP

Internal only.

```text
Pod → Service
```

Not reachable from browser.

---

## NodePort

Exposes Service through Node Port.

Example:

```text
NodeIP:30964
```

Request Flow:

```text
Browser
   ↓
NodePort
   ↓
Service
   ↓
Pod
   ↓
Container
```

---

# Rolling Update Concepts

Image Change:

```yaml
image: fastapi:v1
```

↓

```yaml
image: fastapi:v2
```

Deployment creates:

```text
Old ReplicaSet (v1)
New ReplicaSet (v2)
```

Both ReplicaSets exist during rollout.

---

# Rolling Update Controls

## maxSurge

Extra Pods allowed during update.

Example:

```text
replicas = 3
maxSurge = 1
```

Maximum Pods:

```text
4
```

---

## maxUnavailable

Pods allowed to be unavailable during update.

Example:

```text
replicas = 5
maxUnavailable = 2
```

Minimum Available Pods:

```text
3
```

---

# Core Kubernetes Principles

## Desired State

```text
Desired = 3
Current = 2
```

Kubernetes creates 1 more Pod.

---

## Reconciliation

Controllers constantly compare:

```text
Desired State
vs
Current State
```

and fix differences.

---

## Ownership Chain

```text
Deployment
    ↓ owns
ReplicaSet
    ↓ owns
Pods
```

Delete Pod:

```text
ReplicaSet recreates Pod
```

Delete ReplicaSet:

```text
Deployment recreates ReplicaSet
```

Delete Deployment:

```text
Deployment
ReplicaSet
Pods

All removed
```

---

# Real Production Flow

Developer
↓
Git Push
↓
Jenkins Build
↓
Docker Image
↓
Docker Hub / Registry
↓
Kubernetes Deployment
↓
ReplicaSet
↓
Pods
↓
Service
↓
Users

```
```
# Readiness Probe vs Liveness Probe

Readiness Probe
```text
GET /health
    ↓
200 OK
    ↓
Pod marked Ready
    ↓
Service sends traffic

GET /health
    ↓
5xx / timeout / failure
    ↓
Pod marked Not Ready
    ↓
Service stops sending traffic
```
------------------------------------------------

Liveness Probe
```text
GET /health
    ↓
Success
    ↓
Container keeps running

GET /health
    ↓
Repeated failures
    ↓
Kubernetes restarts container
```