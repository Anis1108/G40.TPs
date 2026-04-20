def handle_client(self, client_socket):

    while True:

        message = client_socket.recv(1024).decode()

        if (not message.endswith("?")
            or len(message) > self.max_message_len
            or "merci" in message):

            client_socket.send("Texte invalide".encode())

        else:

            tokens = self.tokenizer(message, self.vocab)

            response = self.handle_llm(tokens)

            client_socket.send(response.encode())
