# import
from Logic.main import main
from Logic.liste_matier import enregistrement

# vaiables global
from Variables.list import  list_ues


  
if __name__=="__main__" :

    # enregistrement des matières 
    if  list_ues.size_list() == 0:
        enregistrement(list_ues)
        
        
    print("============== liste de ue==================")
    print(list_ues.print_list_eu())
    print("================================")
    main()
   