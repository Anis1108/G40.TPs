TP7 - API REST avec Django

Dans ce TP on a appris à créer une API REST en utilisant Django et Django REST Framework.

On a commencé par créer un projet Django dans le dossier TP7, puis on a créé une application appelée myapi qui contient le code de notre API.

Ensuite on a créé un modèle Message. Ce modèle représente un message dans une petite application de chat. Il contient trois champs :
- source : l'utilisateur qui envoie le message
- to : le destinataire
- body : le contenu du message

Après avoir créé le modèle, on a exécuté les migrations pour créer les tables dans la base de données.

On a aussi utilisé l'interface admin de Django pour ajouter facilement des messages de test.

Ensuite on a installé Django REST Framework pour pouvoir créer une API REST. On a créé un serializer pour transformer les objets Message en JSON et une vue pour gérer les requêtes HTTP comme GET, POST, PUT et DELETE.

On a configuré les URLs pour accéder aux ressources de l'API.

Les principales routes sont :
/messages  : permet de voir ou créer des messages
/users     : permet de voir la liste des utilisateurs

Pour tester l'API on lance le serveur avec la commande :

python manage.py runserver

Ensuite on peut accéder à l'API dans le navigateur :

http://127.0.0.1:8000/messages
http://127.0.0.1:8000/users

Ce TP permet de comprendre les bases de la création d'une API REST avec Django et comment exposer des données via HTTP.
