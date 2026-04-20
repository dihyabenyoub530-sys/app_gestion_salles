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
    from services.services_salle import ServiceSalle
    from models.salle import Salle

    service = ServiceSalle()

    # Ajouter
    salle1 = Salle("B101", "Salle Service", "Classe", 35)
    succes, message = service.ajouter_salle(salle1)
    print(message)

    # Modifier
    salle2 = Salle("B101", "Salle Service Modifiée", "Laboratoire", 40)
    succes, message = service.modifier_salle(salle2)
    print(message)

    # Rechercher
    salle_trouvee = service.rechercher_salle("B101")
    if salle_trouvee:
        print("Salle trouvée :")
        salle_trouvee.afficher_infos()

    print("-------------")

    # Afficher toutes les salles
    liste = service.recuperer_salles()
    for s in liste:
        s.afficher_infos()
        print("-------------")

    # Supprimer
    service.supprimer_salle("B101")
    print("Salle B101 supprimée")