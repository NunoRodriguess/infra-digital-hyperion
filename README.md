# Infrastructure as Code Setup - Local Kubernetes Deployment

This repository contains Helm-based IaC configurations for deploying Digital Hyperion to a local Kubernetes cluster.

## Structure

```
infra-digital-hyperion/
├── helmfile.yaml              # Root helmfile - orchestrates all releases
├── airflow/
│   ├── custom-values.yaml     # Airflow Helm values
│   └── comands.md             # Original deployment commands
├── minio/
│   ├── custom-values.yaml     # MinIO Helm values
│   ├── comands.md             # Original deployment commands
│   └── minio_test.py          # MinIO testing script
└── reddit-scrapper/           # Application layer
    └── scrapper.py
```

## Prerequisites

- Local Kubernetes cluster (already running)
- `kubectl` configured
- `helm` 3.x installed
- `helmfile` installed

### Install Helmfile

```bash
# macOS (Homebrew)
brew install helmfile

# Linux
wget https://github.com/roboll/helmfile/releases/download/v0.144.0/helmfile_linux_amd64
chmod +x helmfile_linux_amd64
sudo mv helmfile_linux_amd64 /usr/local/bin/helmfile

# Or use container image
alias helmfile='docker run --rm -v $(pwd):/workspace -v $HOME/.kube:/root/.kube helmfile:latest'
```

## Deployment Options

### Option 1: Deploy Everything (Recommended for Local Setup)

Deploy both MinIO and Airflow with proper dependency ordering:

```bash
# Add Helm repositories and deploy all releases
helmfile sync

# Or with dry-run first
helmfile diff
helmfile sync
```

### Setup Airflow Secret for GIT Authentication

```bash
# Create Kubernetes secret for Airflow Git authentication
kubectl create secret generic airflow-http-git-secret \
  -n airflow \
  --from-literal=username=your-github-username \
  --from-literal=password=YOUR_GITHUB_TOKEN
```

Change the repository URL in `airflow/custom-values.yaml` to use the secret.
