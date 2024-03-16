# list_ues = [
#         {
#             "titre":"ASD",
#             "duree": 60,
#             "credit": 6
#          },
#         {
#             "titre":"PP",
#             "duree": 60,
#             "credit": 6
#          },
#          {
#             "titre":"PW",
#             "duree": 60,
#             "credit": 6
#          },
#         {
#             "titre":"PS",
#             "duree": 60,
#             "credit": 6
#          },
#         {
#             "titre":"IAP",
#             "duree": 60,
#             "credit": 6
#          },
#          ]

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
   


   # for matier in list_ues:
   #    print(matier.titre)
      