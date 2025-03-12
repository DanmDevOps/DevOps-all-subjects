# DevOps Final Project

## Project Overview

This project implements a complete **CI/CD pipeline** for deploying a **Flask-based microservice** using **Docker, Kubernetes, Terraform, and monitoring tools** like **Prometheus and Grafana**.

## Tech Stack

- **Backend:** Flask (Python)
- **Infrastructure:** Terraform, Kubernetes
- **CI/CD:** GitHub Actions, Docker, Helm
- **Monitoring:** Prometheus, Grafana
- **Security:** SonarQube, Bandit, Trivy
- **Notifications:** Slack Webhooks

## Project Structure

```
.
├── .github/workflows/ci-cd.yml  # CI/CD pipeline definition
├── app/
│   ├── main.py                  # Flask application entry point
│   ├── tests/
│   │   ├── test_main.py         # Unit tests for the app
│   ├── requirements.txt         # Python dependencies
├── helm/
│   ├── chart.yaml               # Helm chart for Kubernetes deployment
│   ├── values.yaml              # Configurations for Helm deployment
├── k8s/
│   ├── deployment.yaml          # Kubernetes deployment configuration
│   ├── service.yaml             # Kubernetes service configuration
├── monitoring/
│   ├── grafana.yaml             # Grafana configuration
│   ├── prometheus.yaml          # Prometheus configuration
├── terraform/
│   ├── main.tf                  # Terraform main configuration
│   ├── variables.tf             # Terraform variables
│   ├── outputs.tf               # Terraform output definitions
├── Dockerfile                   # Docker image setup
├── docker-compose.yaml           # Local containerized development setup
├── README.md                     # Project documentation
```

## CI/CD Pipeline Steps

1. **Linting & Static Analysis**

   - Runs `flake8` and `bandit` to check for style and security issues.
   - Uses **SonarQube** for deep code analysis.

2. **Testing**

   - Runs unit tests with `pytest`.
   - Ensures that the application passes all functional tests before deployment.

3. **Build & Push Docker Image**

   - Builds a Docker image.
   - Scans for vulnerabilities using **Trivy**.
   - Pushes the image to DockerHub.

4. **Deploy to Kubernetes**

   - Uses **Helm** to deploy the application on a **Kubernetes cluster**.
   - Ensures rolling updates and rollback capabilities.

5. **Infrastructure as Code (IaC)**

   - Uses **Terraform** to provision infrastructure.
   - Manages cloud resources (AWS/Azure) for hosting the application.

6. **Monitoring & Logging**

   - Deploys **Prometheus** for system metrics collection.
   - Sets up **Grafana** for visual dashboards.

7. **Notifications**

   - Sends deployment success/failure messages to **Slack** via webhook.

## Running Locally

### Prerequisites

- Python 3.9+
- Docker & Docker Compose
- Kubernetes (Minikube or AWS EKS)
- Terraform CLI



## Authors

- **Dan Monticciolo** ([danmonti117711@gmail.com](mailto\:danmonti117711@gmail.com))

## License

This project is licensed under the MIT License.

