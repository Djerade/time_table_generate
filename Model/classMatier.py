class Matier:
    def __init__(self ) -> None:
        self.titre  = ""
        self.credit  = 0
        self.heure  = 0
        
    def __str__(self) -> str:
        return self.titre + "   " + str(self.credit) + "   " + str(self.heure)
    
    # elle retoutne l'heure restante d'une matier
    def heur_restante(self):
        return self.heure
    
    # Mettre a jour l'heur d'une Matier après chaque séance 
    def update_time(self, hr):
        if (hr <= 3):
            self.heure -= hr
        else:
            self.heure -= 3
    