pipeline {
    agent any

    stages {
        stage('Checkout') {
            echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
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