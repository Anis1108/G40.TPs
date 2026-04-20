import threading

def start_game(self):

    for player in self.players:

        thread = threading.Thread(
            target=self.communicate_with_client,
            args=(player,)
        )

        thread.start()
