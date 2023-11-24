pipeline {
    agent any
    triggers {
        cron ('00 11 * * 6') // Run every Saturday at 11:00 AM
    }
    environment {
        SMTP_CREDENTIALS = credentials('SMTP_CREDENTIALS') 
    }
    stages {
        stage('Clone Repository') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'email_jenkins', url: 'https://github.com/Krishna4537/email_automate.git']])
            }
        }

        stage('Send Maintenance Notification Email') {
            steps {
                script {
                    echo "Starting Send Maintenance Notification Email stage"

                    // Retrieve username and password
                    withCredentials([usernamePassword(credentialsId: 'SMTP_CREDENTIALS', usernameVariable: 'SMTP_CREDENTIALS_USR', passwordVariable: 'SMTP_CREDENTIALS_PSW')]) {
                        echo "Credentials retrieved successfully"
                        def recipients = 'john.smith@test.com,sawhil95@gmail.com,krishna4537@gmail.com'
                        def sender = 'krishna.d190798@gmail.com'
                        def message = 'Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET'
                        def username = SMTP_CREDENTIALS_USR
                        def smtp_server = 'smtp.gmail.com'
                        def password = env.SMTP_CREDENTIALS_PSW
                         // Use the retrieved username and password in the script
                        sh "python3 send_maintenance_email.py '${recipients}' '${sender}' '${message}' '${username}' '${password}' '${smtp_server}'"
                        

                        echo "Python script executed successfully"
                    }
                }
            }
        }
    }
}
