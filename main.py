from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

salle1 = Salle("A101", "Salle Info", "Laboratoire", 25)
dao.insert_salle(salle1)

liste = dao.get_salles()
for s in liste:
    s.afficher_infos()
    print("-------------")
    from Data.dao_salle import DataSalle
    from models.salle import Salle

    dao = DataSalle()


    salle1 = Salle("A102", "Salle Test", "Laboratoire", 20)
    dao.insert_salle(salle1)

    # Modifier une salle
    salle_modifiee = Salle("A102", "Salle Modifiée", "Classe", 30)
    dao.update_salle(salle_modifiee)

    # Rechercher une salle
    s = dao.get_salle("A102")
    if s:
        print("Salle trouvée :")
        s.afficher_infos()

    print("-------------")

    # Afficher toutes les salles
    liste = dao.get_salles()
    for salle in liste:
        salle.afficher_infos()
        print("-------------")

    # Supprimer la salle test
    dao.delete_salle("A102")
    print("Salle A102 supprimée")