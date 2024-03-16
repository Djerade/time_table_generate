class ListtUe():
    def __init__(self) -> None:
      self.list = []
    
    def add_matier(self, ue):
        self.list.append(ue)
        
    def get_list(self):
      return self.list
    
    def size_list(self):
      return len(self.list)