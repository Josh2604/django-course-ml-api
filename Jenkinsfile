pipeline {
    agent any

    stages {
        stage('Dockering app') {
            steps {
	         sh 'docker build --pull --rm -f "compose/local/Dockerfile" -t usersapi:latest .'
            }
        }
        stage('Dockering postgres dependency'){
            steps {
	         sh 'docker build --pull --rm -f "compose/local/postgres/Dockerfile" -t postgresapp:latest .'
            }
        }
        stage('Test'){
            steps{
                sh 'docker-compose -f test.yml up'
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8-alpine3.12'
                }
            }
            steps {
                sh 'python --version'
            }
        }
    }
}