pipeline {
    agent any
    stages {
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
        stage('Test'){
            sh 'python --version'
        }
    }
}