# Créer le 23 mai 2023
# par Nivetha Jeyakumar
# Master IRS P33
# 
# recuperer le nom du sorcier


class GetName:
    def __init__(self):
        self.sorcier = None

    def set_sorcier(self, sorcier):
        self.sorcier = sorcier

    def get_name(self):
        return self.sorcier.name
