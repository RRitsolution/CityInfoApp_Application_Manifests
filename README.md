CityInfo App:-CI-Jenkins/CD-ArgoCD
Tools- JDK-17,Python3,Python3-pip,requests,flask,Jenkins, Docker, Minikube Kubernetes, Arcgo-CD for GitOps CD part

This application is basically based on Python flask web application.  

Application:-CityInfo Function-Enter City Name //It will show temperature and famous places of that City

APIS used-1 API Key to fetch temperature and 1 API Key to fecth famous places

Project Structure:-

city_info_app================================> Main ProjectDirectory
│   ├── app.py===============================> Python application code
│   ├── deploymentservice.yaml===============> kubernetes Manifests file for deployment in k8s cluster
│   ├── Dockerfile===========================> Containerize application 
│   ├── requirements.txt=====================> file for python dependencies
│   └── templates============================> html templates directory for flask                           
│       ├── city_info.html===================> Page to display city info (output page) 
│       └── index.html=======================> Main page (input form for city)


Tools:- 
1-JDK-17 for Jenkins dependencies
2-Python3,Python3-pip Main application tech
3-requests(Call to APIs-temperature & famous places),flask(Web frame work)
4-Jenkins-For CI part-Checkout and pull the codes,then Build and push image to Docker Hub (Why not CD part it will be done by ArgocD)
5-Docker-For container Solution//Build image
6-Minikube- For Application Deployment 
7-ArgoCD for CD part so whenever manifestes file will be synced with Argo CD to ensure deployment



Installation Tools:-

For Python3

If AWS Ubuntu already availbile//check by python3 --version if not
sudo apt install python3 -y
sudo apt install python3-pip(pip acts as package manager for python like APT in linux)


For Open JDK-17
sudo apt update -y
sudo apt upgrade -y
sudo apt install openjdk-17-jdk -y



For Jenkins
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update -y
sudo apt-get install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins

For Docker
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker jenkins// for give permission to Jenkins user to run docker command
newgrp docker//to activate docker group
sudo systemctl restart jenkins

For Kubectl

sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.33/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl

For Minikube(For choice purpose)
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

minikube start --cpus=4 --memory=4096 --driver=docker
minikube status
kubectl get all -n kube-system


For Kubernetes Operator

curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.33.0/install.sh | bash -s v0.33.0
kubectl create -f https://operatorhub.io/install/argocd-operator.yaml
kubectl get csv -n operators

For ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


Argo CD password//

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d


For APIs/Keys -- you can refer SerpApi for City places & openweathermap for temp //form here it has been to take both APIs keys 


For securily use of API keys by Kubernetes secrets

kubectl create secret generic cityinfo-secret --from-literal WEATHER_API_KEY='put api key' --from-literal=PLACES_API_KEY='put api key'


After this setup // needs to run Jenkins pipeline for CI part only-

CD part needs to take care by ArgoCD // Just to configure Github repo(Manifests files) in ArgoCD



