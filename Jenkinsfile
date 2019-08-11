pipeline {
	agent {
		docker { image 'python:rc-alpine'}
	}

	stages {
		stage('build') {

			steps {
				sh 'pip install -r requirements/dev.txt'
			}
		}

		stage('test') {
			steps {
				sh 'python -m unittest discover -v'
				sh 'behave'
			}
		}
	}
}