pipeline {

    agent any

    stages {

        stage('Build Images') {

            steps {

                bat 'docker build -t fastapi-backend .'

            }
        }
        
        stage('Deploy') {

            steps {

                bat 'docker compose up -d'

            }
        }
    }
}