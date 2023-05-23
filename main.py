from set_name import SetName
from get_name import GetName
from fly import Fly
from sort import Sort


# Créer le 23 mai 2023
# par Nivetha Jeyakumar
# Master IRS P33
# 
# main

class Sorcier:
    def __init__(self):
        self.name = None
        self.peut_voler = False
        self.peut_lancer_des_sorts = False



if __name__ == "__main__":
    harry = Sorcier()

    set_name = SetName()
    get_name = GetName()
    fly = Fly()
    sort = Sort()

    set_name.set_sorcier(harry)
    get_name.set_sorcier(harry)
    fly.set_sorcier(harry)
    sort.set_sorcier(harry)

    set_name.set_name("Harry Potter")

    name = get_name.get_name()
    print(f"Nom du sorcier : {name}")

    fly.activer_le_vol()

    sort.activer_les_sorts()

    sort.activer_les_sorts_maudits()

    sort.activer_les_sorts_vegetal()

    print(f"Peut voler : {harry.peut_voler}")
    print(f"Peut lancer des sorts : {harry.peut_lancer_des_sorts}")
    print(f"Peut lancer des sorts maudits : {harry.est_maudit}")
    print(f"Peut manier les plantes : {harry.peut_lancer_des_sorts_vegetal}")

    reponse = input(f"\nVoulez-vous retirer l'utilisation des sorts maudits à {name} ? (o \ n) ")

    if reponse == "o" :
        print(f"\nVous lancez un sort à {name}...")
        sort.desactiver_les_sorts_maudits()
        print(f"{name} peut lancer des sorts maudits : {harry.est_maudit}")
        print(f"{name} n'est plus maudit.\n\n")
    else :
        print(f"Suite à votre réponse, {name} se mit à vous attaquer.")


    print("\n\n------------------------------------------------\n\n")

    bellatrix = Sorcier()
    set_name = SetName()
    get_name = GetName()
    fly = Fly()
    sort = Sort()

    set_name.set_sorcier(bellatrix)
    get_name.set_sorcier(bellatrix)
    fly.set_sorcier(bellatrix)
    sort.set_sorcier(bellatrix)

    set_name.set_name("Bellatrix")

    name = get_name.get_name()
    print(f"Nom du sorcier : {name}")

    fly.activer_le_vol()

    sort.activer_les_sorts()

    sort.activer_les_sorts_maudits()

    sort.activer_les_sorts_vegetal()

    print(f"Peut voler : {bellatrix.peut_voler}")
    print(f"Peut lancer des sorts : {bellatrix.peut_lancer_des_sorts}")
    print(f"Peut lancer des sorts maudits : {bellatrix.est_maudit}")
    print(f"Peut manier les plantes : {bellatrix.peut_lancer_des_sorts_vegetal}")

    reponse = input(f"\nVoulez-vous retirer l'utilisation des sorts maudits à {name} ? (o \ n) ")

    if reponse == "o" :
        print(f"\nVous lancez un sort à {name}...")
        print(f"{name} vous a lancé un sort en retour !!!")

    else :
        print(f"Suite à votre réponse, {name} se mit à rire.")
