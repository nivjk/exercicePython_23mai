from set_name import SetName
from get_name import GetName
from fly import Fly
from sort import Sort


# Créer le 23 mai 2023
# par Nivetha Jeyakumar
# Master IRS P33
# 
# main

def init_sorcier(sorcier, name):
    set_name = SetName()
    get_name = GetName()
    fly = Fly()
    sort = Sort()

    set_name.set_sorcier(sorcier)
    get_name.set_sorcier(sorcier)
    fly.set_sorcier(sorcier)
    sort.set_sorcier(sorcier)

    set_name.set_name(name)

    name = get_name.get_name()
    print(f"Nom du sorcier : {name}")

    fly.activer_le_vol()

    sort.activer_les_sorts()

    sort.activer_les_sorts_maudits()

    sort.activer_les_sorts_vegetal()

    print(f"Peut voler : {sorcier.peut_voler}")
    print(f"Peut lancer des sorts : {sorcier.peut_lancer_des_sorts}")
    print(f"Peut lancer des sorts maudits : {sorcier.est_maudit}")
    print(f"Peut manier les plantes : {sorcier.peut_lancer_des_sorts_vegetal}")

    reponse = input(f"\nVoulez-vous retirer l'utilisation des sorts maudits à {name} ? (o / n) ")

    if reponse == "o":
        print(f"\nVous lancez un sort à {name}...")
        print(f"{name} vous a lancé un sort en retour !!!")

    else:
        print(f"Suite à votre réponse, {name} se mit à rire.")


class Sorcier:
    def __init__(self):
        self.name = None
        self.peut_voler = False
        self.peut_lancer_des_sorts = False



if __name__ == "__main__":
    harry = Sorcier()
    init_sorcier(harry, "Harry Potter")

    print("\n\n------------------------------------------------\n\n")

    bellatrix = Sorcier()
    init_sorcier(bellatrix, "Bellatrix")
