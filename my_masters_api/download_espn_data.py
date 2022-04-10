import os
import sys
import json
import pandas as pd
from database.config import *

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

engine = create_engine(f'postgresql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
Session = sessionmaker(bind=engine) 

os.system("sh update.sh")

with open('data/data_new.json') as json_file:
    data = json.load(json_file)

players = data["players"]


print(players[53])

for index, player in enumerate(players):
    print(index, player["player"])
    if player["cut_element"]=="cut-score":
        cut_score = player["cut_score"]
        players.remove(player)
        # print(f"cut score player{player['player']}")

for player in players:
    print(player["player"])
    if player["thru"]=="CUT":
        # print("CUT")
        player["to_par"] = int(player["tot"])-144
    elif player["thru"]=="WD":
        player["to_par"]=1000
    elif player["to_par"]=="E":
        player["to_par"]=0
    else:
        player["to_par"] = int(player["to_par"])


df = pd.DataFrame.from_records(players).drop(labels=["cut_score","cut_element"], axis="columns")

# print(df)

with Session() as session:
    session.execute("""DELETE FROM espn WHERE 1=1""")
    df.to_sql('espn', con=engine, if_exists='append',index=False)
    session.commit()
    session.close()