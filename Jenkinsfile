pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("myjenkins-blueocean:2.462.1-1")
                }
            }
        }
       
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_credentials') {
                        docker.image("myjenkins-blueocean:2.462.1-1").push("latest")
                    }
                }
            }
        }
    }
}
