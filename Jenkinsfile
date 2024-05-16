pipeline {
    agent any

    environment{
        DOCKER_IMAGE_NAME_FRONTEND = 'review-radar-frontend'
        DOCKER_IMAGE_NAME_BACKEND = 'review-radar-backend'
        GITHUB_REPO_URL = 'https://github.com/kumaranjalij/ReviewRadar.git'
    }

    stages {
        stage('GIT CHECKOUT') {
            steps {
                script {
                        // Checkout the code from the GitHub repo 
                        git branch: 'main', credentialsId: 'ReviewRadar-webhook', url: "${GITHUB_REPO_URL}"
                }
            }
        }
        stage('BACKEND BUILD') {
            steps {
            	sh 'pip install -r requirements.txt'
                sh 'python3 app.py'
            }
        }

        stage('BACKEND TEST') {
             steps {
                 sh 'python3 test_review_analyzer.py'
             }
        }
        
        stage('FRONTEND BUILD') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }

        stage('BUILD DOCKER IMAGES') {
            steps {
                    script {
                        
                        docker.build("${DOCKER_IMAGE_NAME_FRONTEND}", './backend/Review_Radar/')
                    	docker.build("${DOCKER_IMAGE_NAME_BACKEND}", './frontend/reviewradar/')
                    }
            }
        }

        stage('PUSH DOCKER IMAGE') {
            steps {
                script{
                    docker.withRegistry('', 'DockerHubCred') {
                    sh 'docker tag "${DOCKER_IMAGE_NAME_FRONTEND}" anjalijkumar/"${DOCKER_IMAGE_NAME_FRONTEND}":latest'
                    sh 'docker push anjalijkumar/"${DOCKER_IMAGE_NAME_FRONTEND}"'
                    
                    sh 'docker tag "${DOCKER_IMAGE_NAME_BACKEND}" anjalijkumar/"${DOCKER_IMAGE_NAME_BACKEND}":latest'
                    sh 'docker push anjalijkumar/"${DOCKER_IMAGE_NAME_BACKEND}"'
                    }
                }

                //Remove dangling images
                sh "docker image prune -f"
                script {
                    //check if frontend container is already running
                    def isContainerRunning = sh(script: "docker ps -q --filter name="${DOCKER_IMAGE_NAME_FRONTEND}"", returnStatus: true)
                    if(isContainerRunning == 0) {
                        //if container is running stop it
                        sh "docker stop "${DOCKER_IMAGE_NAME_FRONTEND}""
                    }
                    
                    //check if backend container is already running
                    def isContainerRunning = sh(script: "docker ps -q --filter name="${DOCKER_IMAGE_NAME_BACKEND}"", returnStatus: true)
                    if(isContainerRunning == 0) {
                        //if container is running stop it
                        sh "docker stop "${DOCKER_IMAGE_NAME_BACKEND}""
                    }
                }
                //remove frontend container and image
                sh "docker rm "${DOCKER_IMAGE_NAME_FRONTEND}" || true"
                sh "docker rmi -f anjalijkumar/"${DOCKER_IMAGE_NAME_FRONTEND}" || true"
                
                //remove backend container and image
                sh "docker rm "${DOCKER_IMAGE_NAME_BACKEND}" || true"
                sh "docker rmi -f anjalijkumar/"${DOCKER_IMAGE_NAME_BACKEND}" || true"
                

            }
        }

        stage('RUN ANSIBLE PLAYBOOK') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                    )
                }
            }
        }
    }
}
