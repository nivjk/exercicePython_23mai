# Créer le 23 mai 2023
# par Nivetha Jeyakumar
# Master IRS P33
# 
#  activer la capacité à voler

class Fly:
    def __init__(self):
        self.sorcier = None

    def set_sorcier(self, sorcier):
        self.sorcier = sorcier

    def activer_le_vol(self):
        self.sorcier.peut_voler = True

    def desactiver_le_vol(self):
        self.sorcier.peut_voler = False
