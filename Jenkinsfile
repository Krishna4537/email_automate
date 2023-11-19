pipeline {
    agent any
    triggers {
        cron '00 11 * * 6' // Run every Saturday at 11:00 AM
    }
    stages {
        stage('Clone Repository') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'demo_job', url: 'https://github.com/Krishna4537/email_automate.git']])
            }
        }

        stage('Send Maintenance Notification Email') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'smtp-credentials', variable: 'SMTP_CREDENTIALS')]) {
                        def recipients = 'sawhil95@gmail.com,rajshri0999@gmail.com,krishna4537@gmail.com'
                        def sender = 'krishna.d190798@gmail.com'
                        def message = 'Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET'
                        def username = 'krishna.d190798@gmail.com'
                        def smtp_server = 'smtp.gmail.com'

                        sh "python3 send_maintenance_email.py '${recipients}' '${sender}' '${message}' '${username}' '${SMTP_CREDENTIALS}' '${smtp_server}'"
                    }
                }
            }
        }
    }
}
