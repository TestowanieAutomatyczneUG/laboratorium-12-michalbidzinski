

class TemplateEngine:
    def message(self, data):
        pass


class MailServer:
    def send(self, client, data):
        pass

    def receive(self, data):
        pass


class Messenger:
    def __init__(self):
        self.template = TemplateEngine()
        self.mail = MailServer()

    def send(self, client, data):
        return self.mail.send(client, self.template.message(data))

    def receive(self, message):
        return self.mail.receive(message)
