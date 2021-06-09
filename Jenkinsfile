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
	         sh 'docker build --pull --rm -f "compose/local/postgres/Dockerfile" -t postgres_sql:latest .'
            }
        }
        stage('Test'){
            steps{
                sh 'docker-compose -f test.yml up --abort-on-container-exit'
            }
        }
        stage('Sending Notification') {
            steps{
                sh 'Sending notification'
            }
        }
        stage('Cleaning'){
            steps{
                sh 'docker rmi $(docker images -f "dangling=true" -q)'
            }
        }
    }
}