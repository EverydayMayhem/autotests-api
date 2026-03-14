pipeline {
    agent {
        label 'python-agent'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/EverydayMayhem/autotests-api'
            }
        }

	stage('Prepare environment') {
            steps {
                sh 'cp .env.ci .env'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run tests') {
            steps {
                sh 'python3 -m pytest -m regression -n 4'
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