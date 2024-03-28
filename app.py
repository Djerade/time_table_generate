# import
from Logic.main import main
from Logic.input import enregistrement
import os

# vaiables global

from UI.print_screen import print_sreen
from Variables.list import  *
from Variables.compteur import *

if __name__=="__main__" :
   
    # enregistrement des matières 
    if  list_ues.size_list() == 0:
        enregistrement(list_ues)
    print("============== liste des ue ==================")
    print(list_ues.print_list_eu())
    print("nombre des Ue")
    print(list_ues.size_list())
    print("================================")
    main()
    print("================================")
    
    print("Voulez vous un autre  ? Programme 1== oui et 0 == non")
    
    i = int(input())
    while i == 1:
        os.system("cls")
        main()
        print("Voulez vous un autre  ? Programme 1== oui et 0 == non")
        i = int(input())
    print("================================")
