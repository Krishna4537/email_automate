pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Krishna4537/email_automate.git'
            }
        }

        stage('Send Maintenance Notification Email') {
            steps {
                script {
                sh "python send_maintenance_email.py '${params.RECIPIENTS}' '${params.SENDER}' '${params.MESSAGE}'"
                }
            }
        }
    }

    // triggers {
    //     cron '0 0 11 * * SAT' // Run every Saturday at 11:00 AM
    // }
}