import pandas as pd
import numpy as np
import fonctions

def preprocess(games_df):
    games_df["date"] = games_df["date"].astype(str) ; games_df["date"] = games_df["date"].apply(lambda x: x.replace(".", ""))
    games_df["date"] = games_df["date"]=pd.to_datetime(games_df["date"], format="%Y%m%d")
    games_df["perf white"] = games_df["perf white"].astype(str) ; games_df["perf black"] = games_df["perf black"].astype(str)
    games_df[~(games_df["perf white"].isna())]["perf white"] = games_df[~(games_df["perf white"].isna())]["perf white"] .apply(lambda x: fonctions.transform_value(x))
    games_df[~(games_df["perf white"].isna())]["perf black"] = games_df[~(games_df["perf black"].isna())]["perf black"] .apply(lambda x: fonctions.transform_value(x))
    games_df["white elo"] = games_df["white elo"].apply(lambda x: fonctions.transform_elo(x))
    games_df["black elo"] = games_df["black elo"].apply(lambda x: fonctions.transform_elo(x))
    #games_df["number of moves"] = games_df["moves"].apply(lambda x: len(x.split(" ")))
    games_df["opening"] = games_df["ECO"].apply(lambda x: fonctions.match_eco_opening(x))
    games_df["variation"] = games_df["ECO"].apply(lambda x: fonctions.match_eco_variation(x))
    games_df["year"] = games_df["date"].apply(lambda x: x.year) ; games_df.head(2)
    games_df["nb"]=1
    return games_df

