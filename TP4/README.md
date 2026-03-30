# TP4 - Formatage des messages

## Objectif
Dans ce TP, nous avons étudié comment formater les messages échangés entre un client et un serveur dans une application de chat.

Deux formats de données ont été utilisés :
- XML
- JSON

## Partie XML
Nous avons créé un message XML contenant les informations du client :

<client>
    <nom>client1</nom>
    <date_connexion>30/03/2026</date_connexion>
    <lieu>Orsay</lieu>
</client>

Le serveur lit ce message avec la librairie Python `xml.etree.ElementTree` et affiche :
- le nom du client
- la date de connexion
- le lieu de connexion

## Partie JSON
Nous avons également utilisé le format JSON pour envoyer les mêmes informations :

{
  "nom": "client1",
  "date_connexion": "30/03/2026",
  "lieu": "Orsay"
}

Le serveur utilise `json.loads()` pour lire le message et afficher les informations.

## Application de chat
Nous avons proposé plusieurs types de messages pour l'application :

### Identification
{
  "type": "identification",
  "nom": "client1",
  "date_connexion": "30/03/2026",
  "lieu": "Orsay"
}

### Notification
- client connecté
- client déconnecté
- client en train d’écrire

### Etat du client
{
  "type": "etat",
  "nom": "client1",
  "valeur": "LIBRE"
}

Les états possibles sont :
- LIBRE
- OCCUPE
- INACTIF

## Fichiers du TP4
- client.py / serveur.py → XML
- client_json.py / serveur_json.py → JSON
- client_chat.py / serveur_chat.py → application de chat
- test_xml.py → test XML
- test_json.py → test JSON
