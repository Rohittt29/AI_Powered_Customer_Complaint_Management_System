# Deployment Guide

This guide covers the deployment of the AI-Powered Customer Complaint Management System to a production environment.

## Prerequisites

- A Linux server (Ubuntu 22.04 LTS recommended)
- Docker and Docker Compose installed
- Domain name mapped to your server's IP address (optional but recommended)
- Git installed
- External Groq API Key

## 1. Server Setup

SSH into your server and install Docker if you haven't already:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-v2 git
sudo systemctl enable --now docker
```

## 2. Clone Repository

```bash
git clone <your-repository-url> /opt/qms
cd /opt/qms
```

## 3. Configuration

Create the production environment file:

```bash
cp .env.example .env
nano .env
```

Set the following variables:
```ini
ENVIRONMENT=production
LOG_LEVEL=INFO
SECRET_KEY=<generate_a_strong_random_string>
POSTGRES_USER=qms_prod_user
POSTGRES_PASSWORD=<strong_db_password>
POSTGRES_DB=qms_prod_db
GROQ_API_KEY=<your_production_groq_key>
```

## 4. Build and Run Containers

Use the production profile to start the services:

```bash
docker compose --profile prod up -d --build
```

Verify services are running:
```bash
docker compose ps
docker compose logs -f
```

## 5. Database Initialization

Once the database container is up, run the initial migrations and seed the data:

```bash
# Run migrations
docker compose exec backend alembic upgrade head

# Seed initial data (categories, etc.)
docker compose exec backend python scripts/seed_data.py
```

## 6. Reverse Proxy & SSL (Optional but Highly Recommended)

While the system includes Nginx for serving the frontend and proxying API requests, putting it behind a reverse proxy like Caddy or Traefik handles SSL automatically.

Example using Caddy:
Install Caddy and edit `/etc/caddy/Caddyfile`:

```caddyfile
yourdomain.com {
    reverse_proxy localhost:80
}
```

Restart Caddy:
```bash
sudo systemctl restart caddy
```

## 7. Monitoring & Backups

- **Logs:** `docker compose logs -f`
- **Database Backup:** Create a cron job to backup the PostgreSQL volume.
  ```bash
  0 2 * * * docker exec qms_postgres pg_dump -U qms_prod_user qms_prod_db > /backups/qms_db_$(date +\%F).sql
  ```

## 8. CI/CD Updates

The system includes a GitHub Actions pipeline (`.github/workflows/ci.yml`). 
To enable automated deployments, you can add a deployment step in the pipeline that SSHs into the server, pulls the latest code, and runs `docker compose up -d --build`.

For now, manual updates are done via:
```bash
cd /opt/qms
git pull
docker compose --profile prod up -d --build
```
