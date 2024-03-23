# import
from Logic.main import main
from Logic.input import enregistrement

# vaiables global
from UI.print_screen import print_sreen
from Variables.list import  *
from Variables.compteur import *

if __name__=="__main__" :
   
    # enregistrement des matières 
    if  list_ues.size_list() == 0:
        enregistrement(list_ues)
        
        
    print("============== liste de ue==================")
    print(list_ues.print_list_eu())
    print("nombre des matières")
    print(list_ues.size_list())
    print("================================")
    main()
    print_sreen()
    print("================================")
