UDP vs TCP

TCP :
- protocole orienté connexion
- fiable
- garantit l'ordre des messages
- utilisé pour les applications nécessitant fiabilité

UDP :
- protocole sans connexion
- plus rapide
- pas de garantie de livraison
- utilisé pour streaming, jeux, temps réel

Pour passer de TCP à UDP :
- remplacer SOCK_STREAM par SOCK_DGRAM
- utiliser sendto() et recvfrom() au lieu de send() et recv()
