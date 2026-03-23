# TP1 - Les sockets

## 1. Que font les deux scripts ?

### server.py
Le script server.py crée un serveur qui écoute sur une adresse IP et un port.
Il attend qu’un client se connecte, reçoit un message envoyé par le client,
puis envoie une réponse avant de fermer la connexion.

### client.py
Le script client.py crée un client qui se connecte au serveur.
Il envoie un message au serveur, reçoit la réponse et affiche le résultat.


## 2. Quelles sont les différentes fonctions utilisées ?

Les principales fonctions utilisées dans les deux programmes sont :

- socket.socket() : permet de créer une socket
- bind() : associe le serveur à une adresse IP et un port
- listen() : permet au serveur d’attendre les connexions
- accept() : accepte la connexion d’un client
- connect() : permet au client de se connecter au serveur
- send() : envoie un message
- recv() : reçoit un message
- close() : ferme la connexion
- encode() : transforme une chaîne de caractères en bytes
- decode() : transforme les bytes reçus en texte
