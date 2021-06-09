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
               echo 'Sending notification'
            }
        }
        stage('Stoping Services'){
            steps{
                script{
                    try{
                        sh 'docker-compose -f test.yml stop'
                        sh 'docker-compose -f test.yml rm -f'
                    }catch{
                        sh 'Some error stoping services'
                    }
                }
            }
        }
        stage('Cleaning'){
            steps{
                script {
                    try{
                        sh 'docker rm $(docker ps -a -f status=exited -q)'
                        sh 'docker rmi $(docker images -f "dangling=true" -q)'
                    }catch(Exception e){
                        echo 'Some images was not deleted'
                    }
                }
            }
        }
    }
}