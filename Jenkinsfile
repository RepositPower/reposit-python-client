pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh "EXPORT PIPENV_VENV_IN_PROJECT=1 pipenv install"
            }
        }
    }
}