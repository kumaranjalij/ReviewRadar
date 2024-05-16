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
                    sh 'docker tag review-radar-frontend anjalijkumar/review-radar-frontend:latest'
                    sh 'docker push anjalijkumar/review-radar-frontend'
                    
                    sh 'docker tag review-radar-backend anjalijkumar/review-radar-backend:latest'
                    sh 'docker push anjalijkumar/review-radar-backend'
                    }
                }

                //Remove dangling images
                sh "docker image prune -f"
                script {
                    //check if frontend container is already running
                    def isContainerRunning = sh(script: "docker ps -q --filter name=review-radar-frontend", returnStatus: true)
                    if(isContainerRunning == 0) {
                        //if container is running stop it
                        sh "docker stop review-radar-frontend"
                    }
                    
                    //check if backend container is already running
                    def isContainerRunning = sh(script: "docker ps -q --filter name=review-radar-backend", returnStatus: true)
                    if(isContainerRunning == 0) {
                        //if container is running stop it
                        sh "docker stop review-radar-backend"
                    }
                }
                //remove frontend container and image
                sh "docker rm review-radar-frontend || true"
                sh "docker rmi -f anjalijkumar/review-radar-frontend || true"
                
                //remove backend container and image
                sh "docker rm review-radar-backend || true"
                sh "docker rmi -f anjalijkumar/review-radar-backend || true"
                

            }
        }

        stage('RUN ANSIBLE PLAYBOOK') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: './ansible-deploy/deploy.yml',
                        inventory: './ansible-deploy/inventory'
                    )
                }
            }
        }
    }
}
