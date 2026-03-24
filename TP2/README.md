# TP2 UDP vs TCP
### Exercice 1

1. Regrouper le code dans des classes et polymorphisme

Le code a été organisé en deux classes : Server et Client.
La classe Server gère la réception des messages et l’envoi des réponses du côté serveur.
La classe Client permet d’envoyer un message au serveur et de recevoir la réponse.

Le polymorphisme peut être utilisé en créant une classe de base commune dont héritent les classes Server et Client.
Chaque classe peut ensuite redéfinir les méthodes selon son rôle dans la communication.

2. Utilisation de argparse

La bibliothèque argparse permet de lire les arguments donnés lors de l’exécution d’un script Python.
Elle permet d’utiliser un seul fichier de programme pour lancer soit le serveur soit le client selon l’argument fourni par l’utilisateur.
Ainsi, le même script peut être utilisé pour exécuter les deux programmes.

3. 

Pour une application de chat, le protocole TCP est plus adapté.
TCP garantit que les messages arrivent correctement et dans le bon ordre.
