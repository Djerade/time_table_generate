from Model.classMatier import Matier
from rich.console import Console

def enregistrement(list_ue):
   console = Console()
   i = 1
   while(i == 1):
      # Une instance de la classe matière
      ue = Matier()
      print("-----nouvelle matière ------")
      ue.titre = input("titre: ")
      ue.credit = int(input("crédit: "))
      ue.heure =int(input("heure: "))
      list_ue.add_matier(ue)
      print("une autre matière ?  1 == oui /  0 == Non")
      
      i = int(input())


