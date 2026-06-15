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


# Kubernetes ConfigMaps & Secrets - Hands-On Notes

## Goal

Separate application code from configuration.

Follow:

```text
Build Once
Deploy Many Times
```

Instead of creating different Docker images for Dev, QA, and Prod.

---

# Current FastAPI Configuration

Application reads:

```env
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB_NAME
```

Using:

```python
class PostgresSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    db_name: str

    model_config = SettingsConfigDict(env_prefix="POSTGRES_")
```

Application only cares that environment variables exist.

It does NOT care whether they come from:

* .env file
* Docker Compose
* ConfigMap
* Secret
* Jenkins
* Kubernetes

---

# ConfigMap

Used for non-sensitive configuration.

Examples:

```text
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB_NAME
```

Example:

```yaml
apiVersion: v1
kind: ConfigMap

metadata:
  name: postgres-config

data:
  POSTGRES_HOST: db.example.com
  POSTGRES_PORT: "5432"
  POSTGRES_DB_NAME: neondb
```

Apply:

```bash
kubectl apply -f configmap.yaml
```

Verify:

```bash
kubectl get configmap
kubectl describe configmap postgres-config
```

---

# Secret

Used for credentials and sensitive information.

Examples:

```text
POSTGRES_USER
POSTGRES_PASSWORD
```

Example:

```yaml
apiVersion: v1
kind: Secret

metadata:
  name: postgres-secret

type: Opaque

stringData:
  POSTGRES_USER: myuser
  POSTGRES_PASSWORD: mypassword
```

Apply:

```bash
kubectl apply -f secret.yaml
```

Verify:

```bash
kubectl get secret
kubectl describe secret postgres-secret
```

Secrets hide values in describe output.

---

# Injecting ConfigMap and Secret into Pods

Deployment:

```yaml
envFrom:
- configMapRef:
    name: postgres-config

- secretRef:
    name: postgres-secret
```

Flow:

```text
ConfigMap
      +
Secret
      ↓
Pod Environment Variables
      ↓
Pydantic BaseSettings
      ↓
Application
```

Verify inside container:

```bash
kubectl exec -it <pod-name> -- printenv
```

Look for:

```text
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
```

---

# Important Behavior

Changing a ConfigMap or Secret:

```text
DOES NOT
```

automatically update running containers.

Reason:

```text
Environment variables are loaded
when the container starts.
```

Running containers continue using old values.

---

# Common Gotcha

Scenario:

```text
1. Secret contains wrong password
2. Pod starts
3. App fails DB connection
4. Secret fixed
5. kubectl apply secret.yaml
```

Question:

Will Pod automatically use new password?

Answer:

```text
NO
```

Pod must restart.

---

# Why kubectl apply Deployment Did Nothing

Deployment YAML:

```yaml
image: fastapi:v6
```

remained unchanged.

Therefore:

```text
No Deployment change
↓
No ReplicaSet change
↓
No new Pods
```

Kubernetes only reacts to Deployment spec changes.

---

# Solution

Force a rollout:

```bash
kubectl rollout restart deployment/fastapi-deployment
```

This creates new Pods.

New Pods read the latest:

```text
ConfigMap
Secret
```

values.

---

# ReplicaSet Relationship

Changing:

```text
ConfigMap
```

or

```text
Secret
```

does NOT create a new ReplicaSet.

Reason:

ReplicaSets are based on:

```text
Deployment Pod Template
```

Secret contents are external to the Deployment spec.

---

# Production Pattern

Update Secret:

```bash
kubectl apply -f secret.yaml
kubectl rollout restart deployment/app
```

Update ConfigMap:

```bash
kubectl apply -f configmap.yaml
kubectl rollout restart deployment/app
```

---

# Security Notes

Never commit real credentials:

```yaml
POSTGRES_PASSWORD: password
```

to Git.

Kubernetes Secret is NOT a secret manager.

Common production tools:

* HashiCorp Vault
* AWS Secrets Manager
* Azure Key Vault
* Google Secret Manager
* External Secrets Operator

---

# Key Takeaways

```text
ConfigMap
    ↓
Non-sensitive configuration

Secret
    ↓
Credentials

ConfigMap + Secret
    ↓
Environment Variables

Environment Variables
    ↓
Application Configuration
```

```text
ConfigMap/Secret Change
        ≠
Pod Update
```

Need:

```bash
kubectl rollout restart deployment/<deployment-name>
```

for running containers to use new values.

```
```
