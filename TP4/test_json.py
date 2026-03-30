import json

client_str = """
{
    "nom": "client1",
    "date_connexion": "19/04/2026",
    "lieu": "Paris"
}
"""

client = json.loads(client_str)

print("Nom :", client["nom"])
print("Date connexion :", client["date_connexion"])
print("Lieu :", client["lieu"])
