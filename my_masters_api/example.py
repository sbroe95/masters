import json
import pandas as pd
from sqlalchemy import column

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

with open('data/data_new.json') as json_file:
    data = json.load(json_file)

players = data["players"]

for player in players:
    if player["cut_element"]=="cut-score":
        cut_score = player["cut_score"]
        players.remove(player)

df = pd.DataFrame.from_records(players)
print(df)

print(cut_score)

# filename = "competition.csv"

# raw_list = pd.read_csv(filename, header=None)[0].to_list()

# count = 0

# row_list = []
# user_list = []

# for name in raw_list:
#     if count == 4:
#         row_list.append(user_list)
#         count=0
#         user_list = []
#         name = name[:-7]
#     else:
#         if count==0:
#             name = name[:-7]
#     count+=1
#     user_list.append(name)
  

# print(row_list)

# df = pd.DataFrame(row_list, columns=["Gent", "Player 1", "Player 2", "Player 3"])

# dest_filename = "game.csv"
# df.to_csv(dest_filename)
# print(df)
