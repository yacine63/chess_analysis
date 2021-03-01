import pandas as pd
import matplotlib.pyplot as plt

def compute_score_variation(games, color, variation):
    games = games[games["variation"]==variation]
    if color == "white":
        score = (len(games[games["resultat"]=="1-0"]) + 0.5*len(games[games["resultat"]=="1/2-1/2"]))/len(games)
    else:
        score = (len(games[games["resultat"]=="0-1"]) + 0.5*len(games[games["resultat"]=="1/2-1/2"]))/len(games)
    return score


def compute_scored_opening(games, pseudo, opening, color):
    games_with_opening = games[(games[color] == pseudo) & (games["opening"] == opening)]
    print(len(games_with_opening))
    scores = []
    variations = games_with_opening["variation"].value_counts().index.values
    for variation in variations:
        scores.append(compute_score_variation(games_with_opening, color, variation))

    plt.barh(variations, scores)
    plt.xticks(rotation="vertical")
    for index, value in enumerate(scores):
        plt.text(value, index, "{:0.2f}".format(value))
    plt.show()
