import os

list = []

order_data = {
            'auftragsnummer': "bspw",
            'strasse': "straße ",
            'hausnummer': "6",
            'adresszusatz': "",
            'ort': "vehlen",
            'beschreibung': "alles kaputt",
            'email': "nerge@t-online.de",
        }


def file_handling( ):
   
   f = open("auftraege.txt", "w")

    