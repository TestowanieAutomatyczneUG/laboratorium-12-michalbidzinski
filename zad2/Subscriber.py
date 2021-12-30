class Subscriber:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        if type(client) is str:

            self.clients.append(client)
            return self.clients

        else:
            raise TypeError

    def delete_client(self, client):
        if type(client) is not str or client not in self.clients:
            raise ValueError
        self.clients.remove(client)
        return self.clients

    def send_message(self, client, message):
        if type(client) is str and type(message) is str:
            if client in self.clients:
                pass
            else:
                raise ValueError
        else:
            raise TypeError