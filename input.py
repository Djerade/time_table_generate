def inputData():
    # ue_object = {}
    nom_unite = input("nom")
    temps_unite = input("Durée")
    credit_unite = input("Credit")
    ue_object = {
        "Nom": nom_unite,
        "temps": temps_unite,
        "crédit": credit_unite
    } 
    return ue_object
    