# Modules
import random

# import
from Data.liste_jour import jours

# vaiables global
from Variables.list import  *
from Variables.compteur import  *

# Cette fonction fonction retourne le nombre max de semaine
def estimation_duree():
    heure_par_semaine = 54
    heure_total=0
    for ue in list_ues.get_list():
        heure_total += ue.heure
    nbre_semaine = heure_total/heure_par_semaine
    if isinstance(nbre_semaine, float):
        return round(nbre_semaine) + 1
    else:
        return nbre_semaine

   
def main():
     print("semaine estimée")
     print(estimation_duree())
     for i in  range(0, estimation_duree()):
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
                                 
                    else:
                        for ue in list_ues.get_list():
                            if(ue_choose.titre == ue.titre):
                                ue.update_time(ue_choose.heure)
                                # print('heure restant ', ue_choose.heure)
                else:
                    print('temps ecoulé ')       
            emploi_temps_semain.append({
                "nom_jour": jour,
                "ue_jour": martierjournee
            })
            
       
            
        emploi_temps_global.append(emploi_temps_semain)
    

     for x in  emploi_temps_semain:
        print("---" + x['nom_jour']+ "---")
        for ue in x['ue_jour']:
            print("-", ue.titre ," ", ue.heure )
            
            


            
            

    
        
        
    # ue_date = inputData()
    # list_ue.append(ue_date)
    # print(ue_date)
    