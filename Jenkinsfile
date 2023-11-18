pipeline {
    agent any

    parameters {
        string(name: 'RECIPIENTS', defaultValue: 'john.smith@test.com,rodger.more@test.com', description: 'Email Recipients')
        string(name: 'SENDER', defaultValue: 'no-reply-sre@test.com', description: 'Email Sender')
        string(name: 'MESSAGE', defaultValue: 'Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET', description: 'Email Message')
    }

    triggers {
        cron('0 8 * * 6') // Every Saturday at 8 AM
    }

    stages {
        stage('Send Email') {
            steps {
                script {
                    sh "python/email_automate/email.py/email.py '${params.RECIPIENTS}' '${params.SENDER}' '${params.MESSAGE}'"
                }
            }
        }
    }
}