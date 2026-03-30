import xml.etree.ElementTree as ET

client_str = """
<client>
    <nom>client1</nom>
    <date_connexion>19/04/2021</date_connexion>
    <lieu>Paris</lieu>
</client>
"""

root = ET.fromstring(client_str)

print("Tag racine :", root.tag)
print("Nombre d'elements :", len(root))

print("Nom :", root[0].text)
print("Date connexion :", root[1].text)
print("Lieu :", root[2].text)
