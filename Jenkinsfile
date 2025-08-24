pipeline {
  agent any
    
  stages {
    stage('Checkout') {
      steps {
        sh 'echo passed'
        git branch: 'main', url: 'https://github.com/RRitsolution/CityInfoApp.git'
      }
    }
   
    stage('Build and Push Docker Image') {
      environment {
        DOCKER_IMAGE = "nirmaldocker1987/cityinfoapp:${BUILD_NUMBER}"
        // DOCKERFILE_LOCATION = "$WORKSPACE/Dockerfile"
        REGISTRY_CREDENTIALS = credentials('docker-cred')
      }
      steps {
        script {
            sh 'docker build -t ${DOCKER_IMAGE} .'
            def dockerImage = docker.image("${DOCKER_IMAGE}")
            docker.withRegistry('https://index.docker.io/v1/', "docker-cred") {
                dockerImage.push()
            }
        }
      }
    }
    stage('Update Deployment File') {
        environment {
            GIT_REPO_NAME = "CityInfoApp_Application_Manifests"
            GIT_USER_NAME = "RRitsolution"
        }
        steps {
            withCredentials([string(credentialsId: 'github', variable: 'GITHUB_TOKEN')]) {
                sh '''
                    git config user.email "nirmal.elex@gmail.com"
                    git config user.name "Nirmal Shanker"
                    BUILD_NUMBER=${BUILD_NUMBER}
                    sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" $WORKSPACE/deploymentservice.yaml
                    git add $WORKSPACE/deploymentservice.yaml
                    git commit -m "Update deployment image to version ${BUILD_NUMBER}"
                    git push https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} -f HEAD:main
                '''
            }
        }
    }
  }
}
