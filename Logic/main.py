# Modules
import random

# import
from Date.liste_jour import jours

# vaiables global
from Variables.list import  *


def main():
    
     for i in  range(0, 24):
        for jour in  jours:
            martierjournee = []
            for i in range(0, 3):
                ue_choose = random.choice(list_ues.get_list())
                if(ue_choose.heure > 0):
                    martierjournee.append(ue_choose)
                    if (ue_choose.heure <= 3 ):  
                        for ue in list_ues.get_list():
                            if(ue_choose.titre == ue.titre):
                                ue.update_time(ue_choose.heure)
                                print('heure restant ', ue_choose.heure)
                                 
                    else:
                        for ue in list_ues.get_list():
                            if(ue_choose.titre == ue.titre):
                                print("on a trouvé")
                                ue.update_time(ue_choose.heure)
                                print('heure restant ', ue_choose.heure)
                else:
                    print('temps ecoulé ')       
                        


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
    