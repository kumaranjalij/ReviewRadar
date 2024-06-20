
# Review Radar

The project, titled "Review Radar," focuses on leveraging **Natural Language Processing (NLP)** to enhance product development for phone companies by analyzing customer reviews. The primary objective is to understand customer sentiments and pinpoint areas for improvement through topic modeling and sentiment analysis.

The **DevOps** implementation is a core component of the project, aimed at automating and streamlining the development and deployment processes. Key tools used include **Git** for source code management, **Jenkins** for Continuous Integration (CI) and Continuous Deployment (CD), **Docker** for containerization, and **Kubernetes** for orchestrating container deployments. 

**Ansible** is utilized for configuration management, and the **ELK Stack** (Elasticsearch, Logstash, Kibana) ensures continuous monitoring of the system's performance. These practices ensure seamless updates, consistent deployment environments, and real-time insights into system operations.





## File Structure

```bash
ReviewRadar/
├── ansible-deploy/
│   ├── deploy.yml
│   └── inventory
├── backend/
│   └── Review_Radar/
│       └── [backend files]
├── frontend/
│   └── reviewradar/
│       └── [frontend files]
├── k8s/
│   └── [k8s service and deploy files]
└── Jenkinsfile

```


- **backend/Review_Radar/:** Contains backend application code including configuration, models, utilities, and requirements.
- **frontend/reviewradar/:** Contains frontend application code including React components, configuration files, and assets.
- **k8s/:** Contains Kubernetes deployment and service configuration files.
- **ansible-deploy/:** Contains Ansible playbook and inventory files for deployment.
- **Jenkinsfile:** Defines the Jenkins pipeline for CI/CD.


## Tech Stack

### Backend

- **Language:** Python
- **Framework:** Flask (WSGI web application framework)
- **Libraries:**
  - NLTK (Natural Language Toolkit) for sentiment analysis
  - spaCy for advanced Natural Language Processing
  - SQLAlchemy (ORM) for database interactions
  - Flask-CORS for handling Cross-Origin Resource Sharing
  - Joblib for model persistence
- **Logging:** Standard logging for application behavior and errors

### Frontend

- **Language:** JavaScript
- **Library:** React (JavaScript library for building user interfaces)
- **Package Manager:** npm (Node package manager)

### DevOps

- **Version Control:** Git (managed on GitHub)
- **CI/CD:** Jenkins for automation
- **Containerization:** Docker 
- **Orchestration:** Kubernetes
- **Configuration Management:** Ansible
- **Monitoring:** ELK Stack for logging and analytics

### Database

- MySQL for relational database management

### IDEs and Tools

- PyCharm for backend development
- Visual Studio Code (VSCode) for frontend development
- unittest for Python testing
- pip for managing Python dependencies

### Additional Tools

- Ngrok for secure tunnels to localhost during development
- Jenkins Plugins for integration with GitHub, Docker, and other tools



## Deployment

**Prerequisites**

Ensure you have the following installed on the new machine:

- Jenkins
- Docker
- Kubernetes
- Ansible
- Elasticsearch
- Kibana

#

**Clone the project**

```bash
  git clone https://github.com/kumaranjalij/ReviewRadar.git
```

**Go to the project directory**

```bash
  cd ReviewRadar
```

**Configure Jenkins and set up the pipeline script** - steps in [documentation](https://github.com/kumaranjalij/ReviewRadar/blob/main/MT2023126_MT2023072-Report.pdf) 

**Run pipeline script**

- Deployment for this project is automated using a **GitHub webhook trigger** and a **Jenkins pipeline**. 
- When changes are pushed to the repository, the Jenkins pipeline is automatically triggered, running through all stages, including building, testing, containerization, and deployment. This ensures that the latest updates are deployed seamlessly.


## Documentation

[Documentation](https://github.com/kumaranjalij/ReviewRadar/blob/main/MT2023126_MT2023072-Report.pdf) - Step by step implementation of the project.


## Screenshots

![Analysis](https://github.com/kumaranjalij/ReviewRadar/blob/main/Screenshots/Pasted%20image%201.png)

![Analysis Result](https://github.com/kumaranjalij/ReviewRadar/blob/main/Screenshots/Pasted%20image%202.png)

![New Review Analysis](https://github.com/kumaranjalij/ReviewRadar/blob/main/Screenshots/Pasted%20image.png)

![Jenkins pipeline](https://github.com/kumaranjalij/ReviewRadar/blob/main/Screenshots/Screenshot%20from%202024-05-21%2010-32-50.png)

![K8s Dashboard](https://github.com/kumaranjalij/ReviewRadar/blob/main/Screenshots/Screenshot%20from%202024-05-21%2010-34-12.png)


