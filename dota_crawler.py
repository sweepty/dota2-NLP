import csv
import pandas as pd
import requests
from time import sleep
import json
import numpy as np
import re

df = pd.read_csv('id_list.csv')
result = open("dota2_chat2.csv", 'a')
result2 = open("dota_players2.csv", 'a')
result3 = open("dota_matches2.csv", 'a')

csvwriter = csv.writer(result)
csvwriter2 = csv.writer(result2)
csvwriter3 = csv.writer(result3)

csvwriter.writerow(["match_id","time","type","unit","key", "slot","player_slot"])

csvwriter2.writerow([
    "match_id","player_slot","account_id",
    "assists","deaths","denies","gold","gold_per_min","gold_spent",
    "hero_damage","hero_healing","hero_id","kills",
    "level","pings","isRadiant","win","lose","kda"])

csvwriter3.writerow([
    "match_id", "match_seq_num", "radiant_win", "start_time", "duration", "tower_status_radiant", "tower_status_dire", 
    "barracks_status_radiant", "barracks_status_dire","first_blood_time", "positive_votes", "negative_votes",
    "radiant_score", "dire_score"
])

count = 0

for i in range(0, len(df["match_id"])): 
    sleep(1.1)
    match_id = df["match_id"][i]
    url = 'https://api.opendota.com/api/matches/'+str(match_id)
    json_data = requests.get(url).text
    try:
        data = json.loads(json_data)
        count+=1
        try: 
            csvwriter3.writerow([
                data["match_id"], 
                data["match_seq_num"], 
                data["radiant_win"], 
                data["start_time"], 
                data["duration"],
                data["tower_status_radiant"],
                data["tower_status_dire"],
                data["barracks_status_radiant"],
                data["barracks_status_dire"],
                data["first_blood_time"],
                data["positive_votes"],
                data["negative_votes"],
                data["radiant_score"],
                data["dire_score"]
            ])
        except KeyError: 
            pass
                                        
        except ValueError: 
            pass
        
        try: 
            for k in range(0,len(data['chat'])):
                csvwriter.writerow([
                    data["match_id"], 
                    data['chat'][k]['time'],
                    data["chat"][k]["type"],
                    data["chat"][k]["unit"],
                    data["chat"][k]["key"],
                    data["chat"][k]["slot"],
                    data["chat"][k]["player_slot"]
                ])
        except KeyError: 
            pass
                                        
        except ValueError: 
            pass

        
        try:
            for j in range(0, len(data['players'])):
                csvwriter2.writerow([
                    data['players'][j]["match_id"],
                    data['players'][j]["player_slot"],
                    data['players'][j]["account_id"],
                    data['players'][j]["assists"],
                    data['players'][j]["deaths"],
                    data['players'][j]["denies"],
                    data['players'][j]["gold"],
                    data['players'][j]["gold_per_min"],
                    data['players'][j]["gold_spent"],
                    data['players'][j]["hero_damage"],
                    data['players'][j]["hero_healing"],
                    data['players'][j]["hero_id"],
                    data['players'][j]["kills"],
                    data['players'][j]["level"],
                    data['players'][j]["pings"],
                    data['players'][j]["isRadiant"],
                    data['players'][j]["win"],
                    data['players'][j]["lose"],
                    data['players'][j]["kda"]
                ])
        except KeyError: 
            pass

        except ValueError: 
            pass
            print(count,' id:',match_id)

    except json.JSONDecodeError:
        print(match_id,'에서 JSONDecodeError 발생')
        pass

result.close()
result2.close()
result3.close()