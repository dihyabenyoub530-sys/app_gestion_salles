from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

salle1 = Salle("A101", "Salle Info", "Laboratoire", 25)
dao.insert_salle(salle1)

liste = dao.get_salles()
for s in liste:
    s.afficher_infos()
    print("-------------")