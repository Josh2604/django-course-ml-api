pipeline {
    agent any

    stages {
        stage('Check Pipeline') {
            steps {
	         def installed = fileExists '.environment/bin/activate'
              if (!installed) {
                    stage("Install Python Virtual Enviroment") {
                    sh 'virtualenv --no-site-packages .'
              }
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