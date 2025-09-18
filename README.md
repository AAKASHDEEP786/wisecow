# 🐮 Wisecow Application – Kubernetes Deployment with CI/CD & TLS

## 📌 Project Overview
Wisecow is a fun web server that displays random quotes using `fortune` and `cowsay`.  
The goal of this project is to **containerize the Wisecow app**, **deploy it on Kubernetes**, and implement **CI/CD using GitHub Actions**.  
As a challenge goal, the application is also secured with **TLS** using Kubernetes Ingress and cert-manager.

---

## 📂 Project Structure

```text
├── wisecow.sh          # Application script  
├── Dockerfile          # Dockerfile to containerize the app  
├── K8s/  
│   ├── deployment.yaml # Kubernetes Deployment  
│   ├── service.yaml    # Kubernetes Service  
│   └── ingress.yaml    # Ingress with TLS configuration  
└── .github/  
    └── workflows/  
        └── ci-cd.yaml  # GitHub Actions CI/CD pipeline

```
---

## ⚙️ Prerequisites
- Linux environment with Docker installed  
- Kubernetes cluster (Minikube / Kind / Managed K8s)  
- `kubectl` configured to talk to your cluster  
- GitHub account with access to GitHub Actions  
- (Optional for TLS) cert-manager & ingress controller installed  

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/AAKASHDEEP786/wisecow.git
cd wisecow
```

2. Run Locally (Optional)

Install dependencies:
```bash
sudo apt install fortune-mod cowsay -y

#Run the script:

./wisecow.sh
```
Access the app on default port 4499.

---

🐳 Dockerization  

**Build the Docker image**

```bash
docker build -t aakashdevops/wisecow:latest .
```
### Run the container
```bash
docker run -d -p 4499:4499 aakashdevops/wisecow:latest
```
---

☸️ Kubernetes Deployment
### Deploy all manifests
```bash
kubectl apply -f K8s/
```
Verify resources
```bash
kubectl get pods
kubectl get svc
```
Access the application via NodePort/Ingress as configured.

---

🔄 CI/CD Pipeline (GitHub Actions)

### The CI/CD workflow (.github/workflows/ci-cd.yaml) automates:

• Build → Builds the Docker image

• Push → Pushes image to Docker Hub/GHCR

• Deploy → Applies Kubernetes manifests to the cluster (optional)

This ensures the app is continuously deployed whenever changes are pushed to the main branch.

---

🔒 TLS Implementation

• Configured Kubernetes Ingress with TLS termination

• Certificates managed via cert-manager

• Application accessible securely at https://wisecow.devopshackarena.xyz

✅ Expected Artifacts

• Dockerfile → Containerizes the Wisecow app

• K8s Manifests → Deployment, Service, Ingress

• CI/CD Workflow → GitHub Actions automation

• TLS Config → Ingress with HTTPS support

---

📜 License

This project is licensed under the Apache-2.0 License
