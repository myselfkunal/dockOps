# dockOps - Mini Cloud + DevOps Project  
**Containerized Python APIs with Docker Compose + GitHub Actions CI**

## 📌 Overview
This project demonstrates how to containerize **three small Python FastAPI microservices**, connect them using **Docker Compose**, and apply **basic DevOps practices** like Git, automated testing, CI/CD with GitHub Actions, and simple monitoring/logging.  

It is designed as a **beginner-friendly introduction** to Cloud + DevOps concepts in a local environment.

---

## 🧩 Architecture

**Services:**
1. **Auth Service (`auth`)**
   - Provides dummy tokens for users.
   - Endpoint: `/token` → returns `token-<user_id>`.

2. **Products Service (`products`)**
   - Stores a small static product list.
   - Endpoints: `/products`, `/products/{id}`.

3. **Orders Service (`orders`)**
   - Creates orders by:
     - Validating token with `auth`.
     - Fetching product details from `products`.
   - Endpoint: `/orders`.

**Communication:**  
- Services talk to each other via internal Docker Compose networking.  
- `orders` → `auth` (for tokens)  
- `orders` → `products` (for product info)  

---

## 🛠️ Tech Stack
- **Python 3.11** + [FastAPI](https://fastapi.tiangolo.com/)  
- **Docker** + **Docker Compose**  
- **GitHub Actions** (CI: tests + builds)  
- **Pytest** (unit testing)  

---

## 📂 Project Structure
```

project-root/
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

### 1. Clone the repo
```bash
git clone https://github.com/Dking08/dockOps-GFG_Cloud-I.git
cd mini-cloud-devops
````

### 2. Build & start all services

```bash
docker-compose up --build
```

### 3. Test the services

* Check health:

  ```bash
  curl http://localhost:8001/health
  curl http://localhost:8002/health
  curl http://localhost:8003/health
  ```

* Get token:

  ```bash
  curl -X POST http://localhost:8001/token \
       -H "Content-Type: application/json" \
       -d '{"user_id": 1}'
  ```

* Get products:

  ```bash
  curl http://localhost:8002/products
  ```

* Create order:

  ```bash
  curl -X POST http://localhost:8003/orders \
       -H "Content-Type: application/json" \
       -d '{"token":"token-1","product_id":1,"qty":2}'
  ```

---

## ✅ Testing

Each service includes a tiny [pytest](https://docs.pytest.org/) test.
Run tests locally:

```bash
cd auth && pytest
cd products && pytest
cd orders && pytest
```

---

## ⚙️ Continuous Integration (CI)

* CI runs on **GitHub Actions**.
* On every `push` or `pull_request`, it:

  1. Installs dependencies.
  2. Runs unit tests for each service.
  3. Builds Docker images (optional push step).

Workflow file: `.github/workflows/ci.yml`

---

## 📊 Monitoring & Logging

* Logs:

  ```bash
  docker-compose logs -f orders
  ```
* Health endpoints:

  * `GET /health` for each service.

(*Optional: extend with Prometheus + Grafana later.*)

---
