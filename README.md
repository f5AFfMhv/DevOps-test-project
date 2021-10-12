[![CI](https://github.com/f5AFfMhv/DevOps-test-project/actions/workflows/CI.yml/badge.svg)](https://github.com/f5AFfMhv/DevOps-test-project/actions/workflows/CI.yml)

## Context
This projects purpose is to learn following technologies:
* Docker
* Kubernetes
* Cloud
* CI/CD pipelines
* Automatic testing

## Application
Webapp is written with python3 using flask module.  
User can put data to input fields and add them to redis key storage.  
All keys and values stored in redis is displayed in application.

## CI pipeline
Pipeline is made with `GitHubs Actions`.  
Job is triggered by push event. Application syntax is checked with `pylint`. Docker image is build and pushed to docker registry.

## Docker Compose
Run locally with docker-compose
```bash
docker-compose up -d
```

## Kubernetes
Run locally on minikube node
```bash
kubectl apply -f k8s
```