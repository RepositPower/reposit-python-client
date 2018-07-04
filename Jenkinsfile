node('master') {

    checkout scm

    stage('Checkout') {
        steps {
            sh "EXPORT PIPENV_VENV_IN_PROJECT=1 pipenv install"
        }
    }

}