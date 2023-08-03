pipeline {
  agent any
  environment {
    NEXUS_LOGIN=credentials('NEXUS_LOGIN')
  }
  stages {
    stage('build') {
      steps {
        sh "sudo docker build -t localhost8083/pythonapp:latest ."
      }
    }
    stage('push') {
      steps {
        sh "sudo docker login localhost:8083 -u ${NEXUS_LOGIN_USR} -p ${NEXUS_LOGIN_PSW}"
        sh "sudo docker push localhost:8083/pythonapp:latest"
      }
    }
    stage('deploy') {
      steps {
        sh "sudo docker run -d -p 5000:5000 -e SQL_HOST=host.docker.internal --name project1pythonbuild localhost:8083/pythonapp:latest"
      }
    } 
  }
}
