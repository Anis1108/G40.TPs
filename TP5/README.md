\# TP5 - Raw Socket et Modèle OSI



\## Objectif

Ce TP avait pour objectif de travailler avec des \*\*raw sockets\*\*, en manipulant les entêtes \*\*IP\*\* et \*\*TCP\*\* à un niveau bas, comme décrit dans le modèle OSI. Le but était de comprendre comment ces entêtes sont structurées et comment les paquets sont envoyés à travers le réseau.



\## Modifications apportées

\### Serveur

Dans le code fourni, le serveur était basé sur \*\*UDP\*\*. Cependant, le but du TP était d’utiliser des \*\*raw sockets\*\* pour manipuler les entêtes \*\*IP\*\* et \*\*TCP\*\*. J'ai donc modifié le serveur pour qu'il utilise une \*\*raw socket\*\* au lieu de la socket UDP.



\- \*\*Ancienne version\*\* : Utilisation de `socket.SOCK\_DGRAM` pour les sockets UDP.

\- \*\*Nouvelle version\*\* : Changement en `socket.SOCK\_RAW` pour manipuler les paquets au niveau IP et TCP.



\### Client

Le client d’origine envoyait des messages en utilisant des sockets \*\*UDP\*\*. Cependant, pour répondre aux exigences du TP, le client devait créer manuellement les entêtes \*\*IP\*\* et \*\*TCP\*\* et envoyer un paquet via une \*\*raw socket\*\*.



\- \*\*Ancienne version\*\* : Utilisation de sockets \*\*UDP\*\*, sans manipulation des entêtes réseau.

\- \*\*Nouvelle version\*\* : Construction manuelle des entêtes IP et TCP avec la bibliothèque `struct`, puis envoi du paquet via une \*\*raw socket\*\*.



\### Exercices sur les bits

Le code d'origine ne couvrait pas les exercices sur la manipulation des bits. J’ai donc ajouté deux exercices qui manipulent des entiers binaires :



1\. \*\*Compter les bits à 1\*\* : Cette fonction prend un entier en entrée et retourne le nombre de bits à 1 dans sa représentation binaire.

2\. \*\*Échanger deux bits\*\* : Cette fonction permet d’échanger les bits à des positions spécifiques dans un entier.



