from apscheduler.schedulers.blocking import BlockingScheduler
from codeiu import main

if __name__ == "__main__":
    sched = BlockingScheduler()

    
    @sched.scheduled_job('interval', minutes=1)
    def timed_job():
        main.main()
    """
    def timed_job():
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "pythontest420420@gmail.com"  # Enter your address
        receiver_email = "chrisalexeev@gmail.com"  # Enter receiver address
        password = 'pyth0nt35t'
        message = '''\
        Subject: Hi there

        Testing, testing.'''

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    """
    """
    @sched.scheduled_job('cron', day_of_week='mon-sun', hour=13, minute=5)
    def scheduled_job():
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "pythontest420420@gmail.com"  # Enter your address
        receiver_email = "chrisalexeev@gmail.com"  # Enter receiver address
        password = 'pyth0nt35t'
        message = '''\
        Subject: Hi there

        Testing, testing.'''

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    
    """
    sched.start()
    


"""
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == "__main__":
    sched = BlockingScheduler()

    
    @sched.scheduled_job('interval', minutes=10)
    def timed_job():
        account_sid = 'ACe95284b2c0841fe813dd07215053bd48'
        auth_token = '4c2a64c5e82212bee43d1bfa071cd80f'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Chase a check, never chase a bish.",
                            from_='+17653144304',
                            to='+18123916032'
                        )
    

    @sched.scheduled_job('cron', day_of_week='mon-sun', hour=23, minute=15)
    def scheduled_job():
        account_sid = 'ACe95284b2c0841fe813dd07215053bd48'
        auth_token = '4c2a64c5e82212bee43d1bfa071cd80f'
        client = Client(account_sid, auth_token)

        message = client.messages \`
                        .create(
                            body="Chase a check, never chase a bish.",
                            from_='+17653144304',
                            to='+18123916032'
                        )
    

    sched.start()
    """


