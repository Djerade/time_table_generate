class ListUe():
    def __init__(self) -> None:
      self.list = []
    # La fonction qui permet d'ajouter une
    # nouvelle liste dans liste de  matière
    def add_matier(self, ue):
        self.list.append(ue)
    # La fonction qui permet de d'avoir la liste
    # de toutes les matière enregistrées
    def get_list(self):
      return self.list
    # Afficher les ue de la liste
    def print_list_eu(self):
      for ue in self.list:
        print (ue)
        
    # Avoir la toi de la liste
    def size_list(self):
      return len(self.list)