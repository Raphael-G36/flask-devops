# DevOps Project: Flask Deployment (Nginx + Gunicorn + Docker)

## Overview
Production-style deployment of a Flask application, progressing from manual server setup to a fully containerized architecture using Docker.

Demonstrates understanding of how backend services are structured, exposed, and managed in real-world environments.

---

## Architecture

Manual:
Browser → Nginx → Gunicorn → Flask

Dockerized:
Browser → Nginx (container) → Flask (Gunicorn container)

---

## Tech Stack

- Python (Flask)
- Gunicorn
- Nginx
- Linux (WSL)
- Docker
- Docker Compose

---

## Key Implementations

- Deployed Flask app with Gunicorn (production WSGI server)
- Configured Nginx as a reverse proxy
- Managed services using systemd (manual setup)
- Containerized application using Docker
- Built multi-container architecture with docker-compose
- Enabled inter-container communication via service networking

---

## Key Learnings

- Production vs development server architecture
- Reverse proxy design and request flow
- Containerization and image building
- Multi-service orchestration with Docker Compose
- Service isolation and internal networking

---

## Run Locally

### Docker (Recommended)

### bash
git clone <your-repo-url>
cd project2
docker-compose up --build

### Access:
http://localhost
---

## Project Structure
project2/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── nginx/
├── systemd/

## Next Steps
Add environment variable management (.env)
Implement CI/CD pipeline
Deploy to cloud infrastructure (AWS)

Author
Raphael Okonmah
