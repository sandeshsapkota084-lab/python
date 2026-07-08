from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class EmailChannel(NotificationChannel):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSChannel(NotificationChannel):
    def send(self, message):
        print(f"Sending SMS: {message}")

class WhatsAppChannel(NotificationChannel):
    def send(self, message):
        print(f"Sending WhatsApp: {message}")

class PushChannel(NotificationChannel):
    def send(self, message):
        print(f"Sending Push Notification: {message}")

class NotificationService:
    def __init__(self):
        self.channels = []

    def add_channel(self, channel):
        self.channels.append(channel)

    def notify_all(self, message):
        print("Broadcasting message through all channels...")
        for channel in self.channels:
            channel.send(message)
service = NotificationService()
service.add_channel(EmailChannel())
service.add_channel(SMSChannel())
service.add_channel(WhatsAppChannel())
service.add_channel(PushChannel())
service.notify_all("System update scheduled at 10 PM.")