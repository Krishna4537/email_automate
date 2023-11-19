pipeline {
    agent any
    triggers {
        cron '00 11 * * 6' // Run every Saturday at 11:00 AM
    }
    stages {
        stage('Clone Repository') {
            steps {
                // git 'https://github.com/Krishna4537/email_automate.git'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'demo_job', url: 'https://github.com/Krishna4537/email_automate.git']])
            }
        }

        stage('Send Maintenance Notification Email') {
            steps {
                script {
                sh "python3 send_maintenance_email.py '${params.RECIPIENTS}' '${params.SENDER}' '${params.MESSAGE}'"
                }
            }
        }
    }

}