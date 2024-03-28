# Modules
import random

# import
from Data.liste_jour import jours

# vaiables global
from Variables.list import  *
from Variables.compteur import  *

# Cette fonction retourne le nombre max de semaine
def estimation_duree():
    # Nombre d'heure par semaine
    heure_par_semaine = 54
    # Somme de toutes les heure de toutes les matiere enregistrées
    heure_total=0
    for ue in list_ues.get_list():
        heure_total += ue.heure
    nbre_semaine = heure_total/heure_par_semaine
    if isinstance(nbre_semaine, float):
        return round(nbre_semaine) + 1
    else:
        return nbre_semaine

   
def main():
     print("semaine estimée :", estimation_duree())
     numero_semaine = 0
     for i in  range(0, estimation_duree()):
        for jour in  jours:
            # listes de matière prévues dans la journée
            martierjournee = []
            for i in range(0, 3):
                ue_choose = random.choice(list_ues.get_list())
                if(ue_choose.heure > 0):
                    martierjournee.append(ue_choose)
                    # Verification de l'heure restant
                    if (ue_choose.heure <= 3 ):  
                        for ue in list_ues.get_list():
                            if(ue_choose.titre == ue.titre):
                                ue.update_time(ue_choose.heure)
                                 
                    else:
                        for ue in list_ues.get_list():
                            if(ue_choose.titre == ue.titre):
                                ue.update_time(ue_choose.heure)
                                # print('heure restant ', ue_choose.heure)
                
            # Ajout d'un  nouveau programme de la journée dans le programme de la semaine       
            emploi_temps_semain.append({
                "nom_jour": jour,
                "ue_jour": martierjournee
            })
            
       
        # Ajout d'un nouveau programme de la semaine dans le programme global
        emploi_temps_global.append({
            "numero": numero_semaine + 1,
            "semaine": emploi_temps_semain
        })
    

            
            

     for programme_semaine in emploi_temps_global:
        for x in programme_semaine["semaine"]:
            print("---" + x['nom_jour']+ "---")
            for ue in x['ue_jour']:
                print("-", ue.titre ," ",)
     print("---------------------")
     
            
            


            
            

    
        
