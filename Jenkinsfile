pipeline {
  agent any 
  stages {
    stage('build') {
      steps {
        sh "sudo docker build -t localhost8083/project1:jenkinsversion ."
      }
    )
  }
}
