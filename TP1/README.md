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
## 3. Réécriture avec des classes

Les scripts ont été réécrits en utilisant des classes :

- Server : gère la création du serveur et la communication avec le client.
- Client : gère la connexion au serveur et l’échange de messages.

Cette approche permet d’organiser le code de manière plus structurée.
## Chat entre deux clients

Le serveur agit comme intermédiaire entre les clients.

Chaque client se connecte au serveur et envoie des messages.
Le serveur reçoit ces messages et les transmet aux autres clients connectés.

Pour gérer plusieurs clients simultanément, le serveur utilise des threads.
Chaque client est géré dans un thread séparé.
### 4. Si on a plusieurs clients (N clients), quelles modifications faut-il faire ?

Le serveur doit accepter plusieurs connexions et garder une liste des clients connectés.  
Chaque client peut être géré dans un thread différent.  
Quand un client A envoie un message, le serveur peut transmettre ce message au client B.

### 5. Quels sont les inconvénients de cette architecture ?

Le serveur est un point central.  
S’il tombe en panne, la communication s’arrête.  
Si beaucoup de clients se connectent, le serveur peut devenir lent ou surchargé.


