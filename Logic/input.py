from Model.classMatier import Matier

def enregistrement(list_ue):
   i = 1
   while(i == 1):
      ue = Matier()
      print("-----nouvelle matière ------")
      ue.titre = input("titre: ")
      ue.credit = int(input("crédit: "))
      ue.heure =int(input("heure: "))
      list_ue.add_matier(ue)
      print("une autre matier ? 1 == oui /  0 == Non")
      i = int(input())
      
   # print("compter")
   # print(compteur_matiers)
   # for matier in list_ues:
   #    print(matier.titre)


