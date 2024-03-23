# Modules

# import
from Logic.main import main
from Logic.input import enregistrement

# vaiables global
from Variables.list import  *
from Variables.compteur import *


  
if __name__=="__main__" :

    # enregistrement des matières 
    if  list_ues.size_list() == 0:
        enregistrement(list_ues)
    print("============== liste de ue==================")
    print(list_ues.print_list_eu())
    print("taille")
    print(list_ues.size_list())
    print("================================")
    main()
    # print("compter")
    # print(compteur_matiers)
    # print(emploi_temps_mois[0][1].titre)
    # for i in  emploi_temps_mois.items():
    #      print(emploi_temps_mois[i].ue_jour)
   