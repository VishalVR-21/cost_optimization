pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'vishalvr21/cost_optimisation'
        REGISTRY_URL = 'docker.io'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
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