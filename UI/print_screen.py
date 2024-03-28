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
    table = Table(title="Programme")
    console = Console()
    ligne1= []
    ligne2= []
    ligne3= []
    columns = []
    for programme in emploi_temps_global:
        rows = []
        for  objet in programme["semaine"]:
            table.add_column(objet["nom_jour"])
            for ue in objet["ue_jour"]:
                table.add_row(ue.titre)
    
        
            # for row in rows:
            #     table.add_row(row)
            
        console.print(table)
        rows.clear()
        columns.clear()   
            
            
            
    table = Table(title="Programme")
    # for column in columns:
    #     table.add_column(column)
    

    
   
    # for row in rows:
    #     table.add_row(*row, style='bright_green')
    # console = Console()
    # console.print(table)
    # rows.clear()
    # columns.clear()
            

# def print_sreen():
#     from rich.console import Console
#     from rich.table import Table

#     table = Table(title="Programme Générale")
    
#     for programme_semaine in emploi_temps_global:
#         # print("numero:" ,programme_semaine["numero"])
#         table.add_row()
#         for x in programme_semaine["semaine"]:
            
#             # print("---" + x['nom_jour']+ "---")
#             for ue in x['ue_jour']:
#                 # print("-", ue.titre ," ", ue.heure )
#                 table.add_row(ue.titre)
#                 console = Console()
#                 console.print(table)





    # table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    # table.add_column("Title", style="magenta")
    # table.add_column("Box Office", justify="right", style="green")
    # table.add_column("Box Office", justify="right", style="green")

    # table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    # table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    # table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    # table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

    # console = Console()
    # console.print(table)
            




