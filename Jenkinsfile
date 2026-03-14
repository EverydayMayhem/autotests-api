pipeline {
    agent {
        label 'python-agent'
    }

    environment {
        HTTP_CLIENT__URL = "http://test-server:8000"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/EverydayMayhem/autotests-api'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run tests') {
            steps {
                sh 'python -m pytest -m regression -n 4'
            }
        }
    }

    post {
        always {
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]
        }
    }
}