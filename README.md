# 🌐 Enterprise Observability Mesh 

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A production-grade, containerized observability stack built with Docker Compose. This project implements the **Three Pillars of Observability** (Metrics, Logs, and Alerts) for monitoring applications and infrastructure.

## 🏗️ Architecture
* **Prometheus:** Time-series metrics collection and alerting engine.
* **Grafana Loki & Promtail:** Centralized log aggregation and scraping.
* **Grafana:** Unified visualization (Dashboards as Code).
* **Alertmanager:** Alert routing and Discord webhook integration.
* **Node Exporter:** Underlying host OS and hardware metrics.
* **Python Sample App:** Synthetic traffic generator for testing the pipeline.

## 🚀 Quick Start

1. ### Clone this repository:
git clone https://github.com/pradeeprathod1165/enterprise-observability-stack.git
```bash
cd enterprise-observability-stack
```
2. **Configure Alerting:**
Add your Discord Webhook URL in `alertmanager.yml`.

3. ### Bring up the stack

```bash
docker compose up -d
```


4. **Access the Dashboards:**
Navigate to `http://localhost:3000` in your web browser. 
*(Default login: `admin` / `secret`)*

## ✨ Features
* **Infrastructure as Code:** Grafana dashboards and data sources are auto-provisioned via JSON/YAML files on startup.
* **Zero-Code Log Collection:** Promtail reads directly from the Docker socket.
* **Host Monitoring:** Full CPU, RAM, and Disk tracking via Node Exporter.
* **Self-Healing:** Dashboards automatically restore themselves if deleted in the UI.
