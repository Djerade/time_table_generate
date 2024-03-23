from contextlib import contextmanager
from rich import box
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text
from rich.console import Console
from rich.table import Table   
import time

# import
from Data.liste_jour import jours
from Variables.list import *

    # for programme in emploi_temps_global:
    #     for  objet in programme:
    #         objet["nom_jour"]
    #         print(objet["nom_jour"])
    #         for ue in objet["ue_jour"]:
    #             print(ue.titre)
    #             rows.append(ue.titre)



def print_sreen():
    rows = []
    columns = []
    for programme in emploi_temps_global:
        for  objet in programme:
            columns.append(objet["nom_jour"])
            for ue in objet["ue_jour"]:
                rows.append(ue.titre)
            
            
            
    table = Table(title="People")
    for column in columns:
        table.add_column(column)
    
    for column in rows:
        table.add_column(column)
    
   
    for row in rows:
        table.add_row(*row, style='bright_green')
    console = Console()
    console.print(table)
    rows.clear()
    columns.clear()
            




