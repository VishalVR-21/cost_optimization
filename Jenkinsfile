pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'vishalvr21/cost_optimisation'
        REGISTRY_URL = 'docker.io'
    }

    stages {
        stage('Initialize') {
            steps {
                script {
                    // Install Docker
                    sh 'sudo apt update && sudo apt install -y docker.io'
                    
                    // Add Jenkins user to Docker group
                    sh 'sudo usermod -aG docker jenkins || true'
                    
                    // Restart Jenkins to apply changes
                    sh 'sudo service jenkins restart || true'
                    
                    // Verify Docker installation
                    sh 'docker --version'
                }
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh "docker login $REGISTRY_URL -u vishalvr21 -p 12312123Vvr@"
                    sh "docker tag $DOCKER_IMAGE $REGISTRY_URL/$DOCKER_IMAGE"
                    sh "docker push $REGISTRY_URL/$DOCKER_IMAGE"
                }
            }
        }
    }
}
