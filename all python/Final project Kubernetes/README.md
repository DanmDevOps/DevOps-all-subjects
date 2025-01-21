# Dirtbike GIFs Site

This is a simple web application that displays random dirtbike GIFs. The application is built with:
- HTML & JavaScript
- Docker
- Kubernetes
- GitHub Actions for CI/CD

## Getting Started
1. Clone the repository.
2. Build and run the application:
   ```bash
   docker-compose up --build
   ```
3. Visit [http://localhost:8080](http://localhost:8080).

## Deployment
This application is deployed on Kubernetes. See the `k8s-deployment.yaml` file for details.

## CI/CD
The project uses GitHub Actions for CI/CD. Push changes to the `main` branch to trigger the pipeline.
