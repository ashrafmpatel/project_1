pipeline {
  agent any
  environment {
    NEXUS_LOGIN=credentials('NEXUS_LOGIN')
  }
  stages {
    stage('build') {
      steps {
        sh "sudo docker build -t localhost8083/project1:jenkinsversion ."
      }
    }
    stage('push') {
      steps {
        sh "sudo docker login localhost:8083 -u ${NEXUS_LOGIN_USR} -p ${NEXUS_LOGIN_PSW}"
      }
    }
    stage('pull') {
      steps {
        sh "sudo docker pull -t localhost8083/project:1jenkinsversion ."
      }
    }
    }
}
