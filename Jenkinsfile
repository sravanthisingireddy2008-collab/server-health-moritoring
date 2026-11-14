pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Downloading project source code'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t server-health-monitor:latest .'
            }
        }

        stage('Validate Docker Compose') {
            steps {
                bat 'docker compose config -q'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed!'
        }
        always {
            echo 'Pipeline Execution Completed'
        }
    }
}
