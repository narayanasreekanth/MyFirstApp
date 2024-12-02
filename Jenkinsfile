pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "dockersrikahub/myfirstapp"
        DOCKER_REGISTRY_CREDENTIALS = credentials('docker')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: "https://github.com/narayanasreekanth/MyFirstApp.git"
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'docker', toolName: 'docker')  {
                        echo 'Successfully logged in to Docker registry'
                   }
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    try {
                        echo "Building Docker image..."
                        bat """
                            docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                            docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                        """
                    } catch (Exception e) {
                        echo "Error during Docker build: ${e.getMessage()}"
                        throw e
                    }
                }
            }
        }
 
        stage('Docker Push') {
            steps {
                script {
                    try {
                        echo "Pushing Docker image to registry..."
                        bat """
                            docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                            docker push ${DOCKER_IMAGE}:latest
                        """
                    } catch (Exception e) {
                        echo "Error during Docker push: ${e.getMessage()}"
                        throw e
                    }
                }
            }
        }
    }