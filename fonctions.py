import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def transform_value(x):
    try: 
        x = float(x)
        return x
    except ValueError:
        return float(x[1:])
    except TypeError:
        return 0

def transform_elo(elo):
    if elo == "?":
        return None
    elif '?' in elo:
        elo = elo[:-1]
        return int(elo)
    else:
        return elo

def match_eco_opening(eco):
    if eco < "A10":
        return 'Irregular'
    elif eco <= "A40":
        return 'English Opening'
    elif eco <= "A49":
        return "Trompowsky"
    elif eco <= "A79":
        return "Benoni defense"
    elif eco <= "A99":
        return 'Dutch'
    elif eco <"B10":
        return "Alekhine, scandinave and other e4"
    elif eco <= "B19":
        return "Caro-KAnn"
    elif eco <= "B99":
        return "Sicilian"
    elif eco <= "C19":
        return "French"
    elif eco <= "C99":
        return 'e4 e5'
    elif eco <= "D30":
        return "Queen's Gambit"
    elif eco <= "D60":
        return "QGD"
    elif eco <= "D99":
        return "Grunfeld Defence"
    elif eco <= "E20":
        return "Queen's Indian"
    elif eco <= "E59":
        return 'Nimzo Indian'
    elif eco <= "E99":
        return "King's Indian"

def match_eco_variation(eco):
    if eco == "A00":
        return "Irrégulières"
    elif eco == "A01":
        return 'just bad, nothing else'
    elif eco <= "A10":
        return "ouvertures de flanc diverses"
    elif eco <= "A40":
        return 'English'
    elif eco <= "A50":
        return "Trompowsky"
    elif eco <= "A52":
        return 'Budapest'
    elif eco <= "A55":
        return 'old indian'
    elif eco == "A56":
        return "Closed Benoni"
    elif eco <= "A59":
        return "Benko"
    elif eco < "A80":
        return "Benoni Defence"
    elif eco < "A99":
        return "Dutch Defence"
    elif eco == "B00":
        return "Nimzovitch 1.e4 Nc6"
    elif eco == "B01":
        return "Scandinave"
    elif eco <= "B05":
        return "Alekhine"
    elif eco < "B10":
        return "Pirc"
    elif eco < "B20":
        return "Caro-Kann"
    elif eco == "B20":
        return "Morra's Gambit"
    elif eco == "B21":
        return "Grands Prix Attaque"
    elif eco == "B22":
        return "Alapine"
    elif eco <= "B26":
        return "Closed Sicilian"
    elif eco <= "B29":
        return "Sicilian sublines"
    elif eco <= "B31":
        return "Rossolimo"
    elif eco <= "B33":
        return 'Svechnikov'
    elif eco <= "B39":
        return "Accelerated Dragon"
    elif eco <= "B43": 
        return "Kan "
    elif eco <= "B49":
        return "Taimanov"
    elif eco <= "B52":
        return "Moscow variation"
    elif eco <= "B55":
        return "Sicilian sublines"
    elif eco <= "B69":
        return "Dragon variation 5...Nc6"
    elif eco <= "B79":
        return 'Dragon variation 5...g6'
    elif eco <= "B89":
        return 'Scheveninguen'
    elif eco <= "B99":
        return 'Najdorf'
    elif eco == "C00":
        return 'French e4 e6'
    elif eco == "C01":
        return "Exchange variation"
    elif eco == "C02":
        return "Advance variation"
    elif eco <= "C09":
        return "Tarrasch Variation"
    elif eco <= "C14":
        return "Classical variation"
    elif eco < "C20":
        return "Winawer"
    elif eco < "C30":
        return "1.e4 e5 divers"
    elif eco < "C40":
        return "King's Gambit"
    elif eco < "C60":
        return "1.e4 e5 2.Nf3 Nc6"
    elif eco <= "C99":
        return "Spanish"
    elif eco <="D01":
        return "1.d4 d5"
    elif eco == "D02":
        return "London"
    elif eco <= "D05":
        return "1.d4 d5 2.Nf3"
    elif eco == "D07":
        return "Chigorin"
    elif eco <= "D09":
        return 'Albin'
    elif eco <= "D19":
        return "Slave"
    elif eco <= "D30":
        return "QGA"
    elif eco <= "D34":
        return 'Tarrasch'
    elif eco <= "D36":
        return "QGD: exchange variation"
    elif eco <= "D39":
        return "Ragozine"
    elif eco <= "D42":
        return "Semi Tarrasch"
    elif eco <= "D49":
        return "Semi Slave"
    elif eco <= "D52":
        return "Cambridge Springs"
    elif eco <= "D54":
        return 'Orthodox'
    elif eco <= "D57":
        return "Lasker"
    elif eco <= "D59":
        return 'Tatrakover'
    elif eco <= "D69":
        return "orthodox"
    elif eco == "D70":
        return "Grünfeld Saëmisch"
    elif eco <= "D79":
        return "Grünfled Fianchetto variation"
    elif eco <= "D81":
        return "Botvinnik variation"
    elif eco <= "D84":
        return 'Bf4 variation'
    elif eco <= "D89":
        return "Exchange Variation"
    elif eco <= "D91":
        return "Bg5 variation"
    elif eco <= "D93":
        return "Bf4 variation"
    elif eco <= "D95":
        return '5.e3 variation'
    elif eco <= "D99":
        return "Russian variation"
    elif eco <= "E10":
        return "Catalane"
    elif eco <= "E11":
        return "Bogo-Indian"
    elif eco <= "E19":
        return "Queen's Indian"
    elif eco == "E20":
        return 'Romanischine'
    elif eco <= "E29":
        return "Saëmisch"
    elif eco <= "E31":
        return "Nimzo Leningrad"
    elif eco <= "E39":
        return "4.Qc2 variation"
    elif eco <= "E59":
        return "Rubinstein"
    elif eco <= "E61":
        return "King's Indian without e4" 
    elif eco <= "E69": 
        return "King's Indian fianchetto variation"
    elif eco <= "E71":
        return "Makogonov"
    elif eco <= "E75":
        return "Averbakh's variation"
    elif eco <= "E79":
        return "Attaque des 4 pions"
    elif eco <= "E89":
        return "King's Indian Saëmisch"
    elif eco <= "E99":
        return "King's Indian Classical lines"

def find_move_n(moves, n):
    try:
        move = moves.split(" ")[n*2-1]
        return move
    except IndexError:
        return None
