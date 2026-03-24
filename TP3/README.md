## TP3 - Premier serveur

### 1. Liste des clients connectés

Quand un nouveau client se connecte au serveur, celui-ci lui envoie la liste des clients déjà connectés. Le serveur garde une liste des clients afin de pouvoir gérer les communications.

### 2. Notification de déconnexion

Quand un client se déconnecte, le serveur supprime ce client de la liste des clients connectés et envoie une notification aux autres clients pour les informer de cette déconnexion. La notification contient le nom du client qui s'est déco>

### 3. Choix de l’interlocuteur

Avant d’envoyer un message, le client doit choisir le destinataire. Le message est envoyé au serveur qui le transmet uniquement au client concerné.

