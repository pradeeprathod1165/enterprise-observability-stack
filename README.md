# Enterprise Observability Mesh 

A production-grade, containerized observability stack built with Docker Compose. This project implements the "Three Pillars of Observability" (Metrics, Logs, and Alerts) for monitoring applications and infrastructure.

## Architecture
* **Prometheus:** Time-series metrics collection and alerting engine.
* **Grafana Loki & Promtail:** Centralized log aggregation and scraping.
* **Grafana:** Unified visualization (Dashboards as Code).
* **Alertmanager:** Alert routing and Discord webhook integration.
* **Node Exporter:** Underlying host OS and hardware metrics.
* **Python Sample App:** Synthetic traffic generator for testing the pipeline.

## Quick Start
1. Clone this repository.
2. Add your Discord Webhook URL in `alertmanager.yml`.
3. Bring up the stack:
   \`\`\`bash
   docker compose up -d
   \`\`\`
4. Access Grafana at `http://localhost:3000` (Default login: admin / secret).

## Features
* **Infrastructure as Code:** Grafana dashboards and data sources are auto-provisioned via JSON/YAML files on startup.
* **Zero-Code Log Collection:** Promtail reads directly from the Docker socket.
* **Host Monitoring:** Full CPU, RAM, and Disk tracking via Node Exporter.
* **Self-Healing:** Dashboards automatically restore themselves if deleted in the UI.
