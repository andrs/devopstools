pipeline {
    agent any // any agent can run this job

      environment {
            // Define el nombre de la imagen que se construirá.
            DOCKER_IMAGE = "andrs/flaskapi"
        }

    stages {
        stage('Echo Hello World') {
            steps {
                echo 'Hello World'
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Usamos el helper 'withRegistry' para manejar la autenticación.
                    // 'dockerhub-credentials' es el ID de la credencial en Jenkins.
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {

                    // Construye la imagen usando el Dockerfile del repositorio.
                    def customImage = docker.build(DOCKER_IMAGE)

                    // Sube la imagen a Docker Hub con dos etiquetas:
                    // 1. La etiqueta 'latest' para la versión más reciente.
                    // 2. Una etiqueta con el número de build para versionado.
                    customImage.push()
                        customImage.push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }

    }
    post {
        always {
            cleanWs() // clean workspace when done
        }
    }
}