🚀 CityInfo App – CI/CD Project

CI → Jenkins

CD → ArgoCD (GitOps)

🔹 Tools & Technologies

JDK 17 → for Jenkins dependencies

Python3, pip → core application stack

Flask → lightweight web framework

Requests → API calls (temperature & famous places)

Jenkins → CI (checkout, build & push Docker image)

Docker → container solution

Minikube (Kubernetes) → application deployment

ArgoCD → GitOps CD (sync manifests & ensure deployment)

🔹 Application Overview

Based on → Python Flask web app

Function → User enters city name → App displays:

🌡️ Temperature

📍 Famous places

APIs Used →

OpenWeatherMap → fetch temperature

SerpApi → fetch famous places

🔹 Project Structure
city_info_app/
├── app.py                  --> Python Flask application code
├── deploymentservice.yaml  --> Kubernetes manifest (deployment)
├── Dockerfile              --> Containerization
├── requirements.txt        --> Python dependencies
└── templates/              --> HTML templates
    ├── index.html          --> Input form (city name)
    └── city_info.html      --> Output page (city info)

🔹 Installation Steps

Python3 & pip

sudo apt install python3 -y
sudo apt install python3-pip -y


OpenJDK 17

sudo apt update -y && sudo apt upgrade -y
sudo apt install openjdk-17-jdk -y


Jenkins

wget -O /etc/apt/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list
sudo apt-get update -y && sudo apt-get install jenkins -y
sudo systemctl enable --now jenkins


Docker

sudo apt install docker.io -y
sudo usermod -aG docker jenkins
newgrp docker
sudo systemctl restart jenkins


Kubectl

sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.33/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update && sudo apt-get install -y kubectl


Minikube

curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start --cpus=4 --memory=4096 --driver=docker


ArgoCD

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


Retrieve Argo CD password:

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

🔹 Secure API Keys via Kubernetes Secrets
kubectl create secret generic cityinfo-secret \
  --from-literal=WEATHER_API_KEY='your_weather_key' \
  --from-literal=PLACES_API_KEY='your_places_key'

🔹 CI/CD Workflow

CI (Jenkins):

Pull source code

Build Docker image

Push image to Docker Hub

CD (ArgoCD):

Syncs Kubernetes manifests from GitHub

Automatically ensures latest deployment

<img width="747" height="298" alt="image" src="https://github.com/user-attachments/assets/0fd0cbc3-3213-433d-8a55-21db386cd43c" />

