#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Building and pushing Docker image..."
docker build -t username/dirtbike-gifs:v1 .
docker push username/dirtbike-gifs:v1

echo "Applying Kubernetes configurations..."
kubectl apply -f k8s-deployment.yaml

echo "Deployment complete!"
kubectl get services
