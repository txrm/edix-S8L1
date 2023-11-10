pipeline {
    agent none

    stages {
        stage('Non-Parallel Stage') {
            agent any
            steps {
                echo 'Message from built in node.'
            }
        }

        stage('Parallel Stages') {
            parallel {
                stage('Python Stage') {
                    agent {
                        docker {
                            image 'python:latest'
                        }
                    }
                    steps {
                        echo 'Running Python container...'
                    }
                    post {
                        success {
                            echo 'Python container stage succeeded!'
                        }
                        failure {
                            echo 'Python container stage failed. Check internet connection.'
                        }
                    }
                }

                stage('Node.js Stage') {
                    agent {
                        docker {
                            image 'node:latest'
                        }
                    }
                    steps {
                        echo 'Running Node.js container...'
                        sh 'node --version'
                    }
                    post {
                        success {
                            echo 'Node.js container stage succeeded!'
                        }
                        failure {
                            echo 'Node.js container stage failed. Check internet connection.'
                        }
                    }
                }
            }
        }

        stage('End') {
            agent any
            steps {
                echo 'Containers downloaded.'
            }
        }
    }
}
