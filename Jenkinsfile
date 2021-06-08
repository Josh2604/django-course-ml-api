pipeline {
    agent any

    stages {
        stage('Hello World Pipeline') {
            steps {
	         echo "Hello world"
            }
        }
        stage('Test'){
            steps{
               sh 'virtualenv env'
               sh'''#!/bin/bash
                     source env/bin/activate
               '''
               sh 'pip install --upgrade -r requirements/production.txt'
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