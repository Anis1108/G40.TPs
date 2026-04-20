def communicate_with_client(self, client_id):

    while True:

        send(client_id, "Choisissez 1, 2 ou 3 bâtonnets à retirer")

        message = read()

        if not message.isdigit():

            send(client_id, "Erreur")
            continue

        number = int(message)

        if number < 1 or number > 3:

            send(client_id, "Erreur")
            continue

        self.nbr_sticks -= number

        if self.nbr_sticks > 0:

            send(client_id, "vous restez dans le jeu")

        else:

            send(client_id, "perdu")

            for player in self.players:

                if player != client_id:

                    send(player, "gagné")

            break
