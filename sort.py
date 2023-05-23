# Créer le 23 mai 2023
# par Nivetha Jeyakumar
# Master IRS P33
# 
# activer les sorts

class Sort:
    def __init__(self):
        self.sorcier = None

    def set_sorcier(self, sorcier):
        self.sorcier = sorcier

    def activer_les_sorts(self):
        self.sorcier.peut_lancer_des_sorts = True

    def desactiver_les_sorts(self):
        self.sorcier.peut_lancer_des_sorts = False

    def activer_les_sorts_maudits(self):
        self.sorcier.est_maudit = True

    def desactiver_les_sorts_maudits(self):
        self.sorcier.est_maudit = False

    def activer_les_sorts_vegetal(self):
        self.sorcier.peut_lancer_des_sorts_vegetal = True

    def desactiver_les_sorts_vegetal(self):
        self.sorcier.peut_lancer_des_sorts_vegetal = False