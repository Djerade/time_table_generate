class Matier:
    def __init__(self ) -> None:
        self.titre  = ""
        self.credit  = 0
        self.heure  = 0
        
    
    def heur_restante(self):
        return self.heure
    def update_time(self, hr):
        if (hr == 3):
            self.heure -= 3
        else:
            self.heure -= hr
    