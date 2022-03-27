pipeline {
    agent { label 'agent_1' }
    stages {
        stage('CheckOut'){
            steps{
                git url: 'https://github.com/ben-gutman/WorldOfGames.git', branch: 'main'
            }
        }
         stages {
        stage('Build'){
            steps{
                sh 'docker build -t my-flask .'
            }
        }
        stage('Run & Test') {
            agent {
                docker {
                    image "my-flask"
                    reuseNode true
                }
            }
            steps {
                sh 'python3 /app/MainScores.py &'
                sh 'sleep 5'
                sh 'python3 e2e.py'
            }
        }
    }
}