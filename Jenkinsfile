pipeline {

    agent any

    stages {

        stage('Environment Check') {

            steps {

                bat 'git --version'
                bat 'docker --version'

            }
        }

    }
}