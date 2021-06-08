pipeline {
    agent any

    stages {
        stage('Hello World Pipeline') {
            steps {
	         echo "Hello world"
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8-alpine3.12'
                }
            }
            steps {
                sh 'python3 -venv .env'
                sh 'source .env/bin/activate'
                sh 'pip install -r requirements/production.txt'
                sh 'python3 manage.py test'
            }
        }
    }
}