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

        stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t vishalvr21/cost_optimisation ."
                }
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