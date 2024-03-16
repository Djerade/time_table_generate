from Model.list_matier import ListtUe
import random


# import
# from liste_matier import list_ues
from liste_jour import jours
from liste_matier import enregistrement

if __name__=="__main__" :
    emploi_temps_semain= []   
    emploi_temps_mois= [] 
    list_ues = ListtUe()
    if list_ues.size_list() == 0:
        enregistrement(list_ues)
    for i in  range(0, 1):
        for jour in  jours:
            martierjournee = []
            for i in range(0, 3):
                ue_choose = random.choice(list_ues.get_list())
                if(ue_choose.heure > 0):
                    martierjournee.append(ue_choose)
                    if (ue_choose.heure <= 3 ):  
                        for ue in list_ues:
                            if(ue_choose.titre == ue.titre):
                                ue.titre = 0
                                 
                                
                
                    for ue in list_ues:
                        if(ue_choose.titre == ue.titre):
                            print("on a trouvé")
                            ue.hour()


            emploi_temps_semain.append({
                "nom_jour": jour,
                "ue_jour": martierjournee
            })
            # print({
            #     "nom_jour": jour,
            #     "ue_jour": martierjournee
            # })
            
        emploi_temps_mois.append(emploi_temps_semain)
    
    
    
    for x in  emploi_temps_semain:
        print("---" + x['nom_jour']+ "---")
        for ue in x['ue_jour']:
            print("-", ue.titre ," ", ue.heure )

            
            
    # for emploi in  emploi_temps_mois:
    #     print(emploi)
            
    
        
        
    # ue_date = inputData()
    # list_ue.append(ue_date)
    # print(ue_date)
    