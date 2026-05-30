pipeline {

    agent any

    stages {

        stage('Build Images') {

            steps {

                bat 'docker build -t fastapi-backend .'

            }
        }

    }
}