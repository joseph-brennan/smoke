pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        withEnv(['CHROME_BIN=chromium-browser', 'DISPLAY=:99.0']) {
          sh "sh -e /etc/init.d/xvfb start"
          sh "bash -c \".travis/run.sh \""
        }
      }
    }
  }
}
