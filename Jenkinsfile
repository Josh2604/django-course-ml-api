pipeline {
    agent any

    stages {
        stage('Check Pipeline') {
            steps {
	         sh 'Checking env'
            }
        }
        stage('Test'){
            steps{
               sh 'virtualenv env && source env/bin/activate && pip install --upgrade -r requirements/production.txt'
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