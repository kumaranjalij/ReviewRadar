pipeline {
    agent any

    environment{
        DOCKER_IMAGE_NAME_FRONTEND = 'anjalijkumar/review-radar-frontend'
        DOCKER_IMAGE_NAME_BACKEND = 'anjalijkumar/review-radar-backend'
        GITHUB_REPO_URL = 'https://github.com/kumaranjalij/ReviewRadar.git'
        DOCKERHUB_CREDENTIALS = credentials('DockerHubCred')
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
		// Activate the virtual environment
		withEnv(['PATH+VENV=/var/lib/jenkins/workspace/ReviewRadar/rrenv/bin']) {
		    // Install packages from requirements.txt within the virtual environment
		    sh 'python3 -m nltk.downloader vader_lexicon'
		    sh 'python3 -m spacy download en_core_web_sm'
		    
		    sh 'pip install -r ./backend/Review_Radar/requirements.txt'

		    // Run your Python script within the virtual environment
            	    sh 'nohup python3 ./backend/Review_Radar/app.py > app.log 2>&1 &'
		}
	    }
	}


	//stage('BACKEND TEST') {
	  //  steps {
		// Activate the existing Python environment
		//withEnv(['PATH+VENV=/var/lib/jenkins/workspace/ReviewRadar/rrenv/bin']) {
		    // Run your test script
		  //  sh 'python3 ./backend/Review_Radar/test_review_analyzer.py'
		//}
	    //}
	//}

        
        stage('FRONTEND BUILD') {
	    steps {
		// Change directory to your specific directory
		dir('./frontend/reviewradar/') {
		    // Run npm install and npm run build commands
		    sh 'npm install'
		    sh 'npm run build'
		}
	    }
	}


        stage('BUILD DOCKER IMAGES') {
            steps {
        	script {
        	     // Build and tag backend Docker image
                     //docker.build("${DOCKER_IMAGE_NAME_BACKEND}", './backend/Review_Radar/')
                     sh 'docker build -t "${DOCKER_IMAGE_NAME_BACKEND}" ./backend/Review_Radar/'
                        
                     // Build and tag frontend Docker image
                     //docker.build("${DOCKER_IMAGE_NAME_FRONTEND}", './frontend/reviewradar/')
                     sh 'docker build -t "${DOCKER_IMAGE_NAME_FRONTEND}" ./frontend/reviewradar/'
                }
            }
        }

        stage('PUSH DOCKER IMAGE') {
            steps {
                script{
                    sh 'echo "Logging in to Docker Hub"'
                    sh """
                    echo \$DOCKERHUB_CREDENTIALS_PSW | docker login -u \$DOCKERHUB_CREDENTIALS_USR --password-stdin
                    """
                    
                    sh 'echo "pushing frontend"'
                    sh 'docker push anjalijkumar/review-radar-frontend:latest'
                    
                    sh 'echo "pushing backend"'
                    sh 'docker push anjalijkumar/review-radar-backend:latest'
                    
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
