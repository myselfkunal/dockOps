# dockOps - Mini Cloud + DevOps Project  
**Containerized Python APIs with Docker Compose + GitHub Actions CI**

## 📌 Overview
**dockOps** is a hands-on DevOps project that demonstrates how to design, containerize, and connect multiple backend microservices using Docker and Docker Compose, with automated validation using GitHub Actions CI.

The project is intentionally kept simple while following **real-world DevOps practices**, making it ideal for learning and showcasing cloud-native fundamentals.
---

## 🧩 Architecture

The system consists of **three independent FastAPI microservices**:

### 🔐 Auth Service
- Generates and validates user tokens
- Endpoints:
  - `GET /token?user_id=<id>`
  - `GET /validate?token=<token>`

### 📦 Products Service
- Stores a static list of products
- Endpoints:
  - `GET /products`
  - `GET /products/{id}`

### 🧾 Orders Service
- Creates orders by:
  - Validating tokens via Auth service
  - Fetching product details via Products service
- Endpoint:
  - `POST /orders`

### 🔗 Service Communication
Services communicate over an internal Docker network:

- `orders → auth`
- `orders → products`

---

## 🛠️ Tech Stack

- **Python 3.11**
- **FastAPI**
- **Docker & Docker Compose**
- **Git & GitHub**
- **GitHub Actions (CI)**
- **HTTPX (service-to-service communication)**

---

## 📂 Project Structure
```

dockOps/
├─ auth/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ products/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ orders/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ docker-compose.yml
└─ .github/workflows/ci.yml

````


---

## 🚀 Getting Started

### Prerequisites
- Docker
- Docker Compose

### 1️⃣ Clone the repository
```bash
git clone https://github.com/myselfkunal/dockOps.git
cd dockOps

````

### 2. Build & start all services

```bash
docker-compose up --build
```

### 3. Test the services

* Generate token:

  ```bash
  curl "http://localhost:8000/token?user_id=kunal"
  ```

* Get products:

  ```bash
  curl http://localhost:8001/products
  ```

* Create an order:

  ```bash
  curl -X POST http://localhost:8002/orders \
  -H "Content-Type: application/json" \
  -d '{
    "token": "<PASTE_TOKEN_HERE>",
    "product_id": 1
  }'
  ```

---

## ⚙️ Continuous Integration (CI)

* This project uses **GitHub Actions** to automatically validate the system.
* On every `push` or `pull_request`, the CI pipeline:

  1. Builds Docker images.
  2. Starts all services using Docker Compose.
  3. Runs smoke tests against live containers.
  4. Fails fast if any service is broken. 

Workflow file: `.github/workflows/ci.yml`

---

## 📈 What This Project Demonstrates

   1. Microservices architecture basics
   2. Containerization with Docker
   3. Service-to-service communication
   4. Token-based authentication
   5. Docker Compose orchestration
   6. CI pipelines using GitHub Actions
   7. Clean Git branching and workflow practices


---
