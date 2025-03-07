pipeline {
    agent any

    environment {
        // Replace with your actual Docker Hub username and Jenkins credentials ID
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
        DOCKERHUB_REPO = 'yourdockerhubusername/ml-cicd-project'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/yourusername/ml-cicd-project.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${env.DOCKERHUB_REPO}:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', env.DOCKERHUB_CREDENTIALS) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
    post {
        success {
            // Email notification on successful deployment (ensure Email Extension Plugin is configured in Jenkins)
            emailext subject: "Deployment Successful",
                     body: "The ML project has been successfully deployed from the master branch via Jenkins.",
                     to: "admin@example.com"  // Replace with the admin's email address
        }
    }
}
