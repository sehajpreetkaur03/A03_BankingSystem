# client/client.py
from datetime import datetime
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email

class Client(Observer):
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def update(self, message):
        subject = f"ALERT: Unusual Activity: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        body = f"Notification for {self._email}: {self._name}: {message}"
        simulate_send_email(subject, body)
