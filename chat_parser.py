import json
import csv
import requests
from time import sleep

result = open("chat.csv", 'a')
csvwriter = csv.writer(result)
csvwriter.writerow(["match_id", "time","type","key", "player_slot"])

def jsonToCsv(s_date, e_date):
    url = 'https://api.opendota.com/api/explorer?sql=SELECT%0Amatch_id%2C%0Achat%0AFROM%20matches%0AWHERE%20TRUE%0Aand%20chat%20is%20not%20null%0AAND%20start_time%20%3E%3D%20extract(epoch%20from%20timestamp%20%27'+str(s_date)+'T00%3A00%3A00.000Z%27)%0AAND%20start_time%20%3C%20extract(epoch%20from%20timestamp%20%27'+str(e_date)+'T00%3A00%3A00.000Z%27)%0AORDER%20BY%20match_id%20NULLS%20LAST'
    json_data = requests.get(url).text
    data = json.loads(json_data)
            
    for xx in range(0, len(data["rows"])):
        if data["rows"][xx]["chat"] != None:
            for i in range(0,len(data["rows"][xx]['chat'])):
                try: 
                    csvwriter.writerow([
                        data["rows"][xx]["match_id"], 
                        data["rows"][xx]["chat"][i]["time"],
                        data["rows"][xx]["chat"][i]["type"],
                        data["rows"][xx]["chat"][i]["key"],
                        data["rows"][xx]["chat"][i]["player_slot"]
                    ])
                    # with result as outf:
                    #     csvwriter.writerow([
                    #             data["rows"][xx]["match_id"], 
                    #                 data["rows"][xx]["chat"][i]["time"],
                    #                 data["rows"][xx]["chat"][i]["type"],
                    #                 data["rows"][xx]["chat"][i]["key"],
                    #                 data["rows"][xx]["chat"][i]["player_slot"]
                    #     ])
                except KeyError: 
                    pass
                    # print('err')
                    # print('에러')
                        
                except ValueError: 
                    # print('err')
                    pass
                # finally:
                #     result.close()
                
    

for i in range(2015, 2018):
    if i == 2015:
        for j in range(9,11):
            sleep(20)
            s_date = str(i) + "-" +str(j)+ "-10"
            e_date = str(i) + "-" +str(j+1)+ "-10"

            print(s_date, e_date)
            jsonToCsv(s_date, e_date)
    # elif i == 2018:
    #     for j in range(0,3):
    #         if j == 0:
    #             i -= 1
    #             j = 12
    #         s_date = str(i) + "-" +str(j)+ "-10"
    #         e_date = str(i) + "-" +str(j+1)+ "-10"
    #         print(s_date, e_date)
    #         jsonToCsv(s_date, e_date)

    else:
        for j in range(0, 12):
            sleep(20)
            # sleep(30)
            if j == 0:
                i -= 1
                j = 12
            s_date = str(i) + "-" +str(j)+ "-10"

            if j == 12:
                i += 1
                j = 0

            e_date = str(i) + "-" +str(j+1)+ "-10"
            print(s_date, e_date)
            jsonToCsv(s_date, e_date)
    result.close()
# with result as outf:
    #     # csvwriter = csv.writer(result)
    #     url = 'https://api.opendota.com/api/explorer?sql=SELECT%0Amatch_id%2C%0Achat%0AFROM%20matches%0AWHERE%20TRUE%0Aand%20chat%20is%20not%20null%0AAND%20start_time%20%3E%3D%20extract(epoch%20from%20timestamp%20%27'+str(s_date)+'T00%3A00%3A00.000Z%27)%0AAND%20start_time%20%3C%20extract(epoch%20from%20timestamp%20%27'+str(e_date)+'T00%3A00%3A00.000Z%27)%0AORDER%20BY%20match_id%20NULLS%20LAST'
    #     json_data = requests.get(url).text
    #     data = json.loads(json_data)
            
    #     for xx in range(0, len(data["rows"])):
    #         if data["rows"][xx]["chat"] != None:
    #             for i in range(0,len(data["rows"][xx]['chat'])):
    #                 try: 
    #                     csvwriter.writerow([
    #                             data["rows"][xx]["match_id"], 
    #                             data["rows"][xx]["chat"][i]["time"],
    #                             data["rows"][xx]["chat"][i]["type"],
    #                             data["rows"][xx]["chat"][i]["key"],
    #                             data["rows"][xx]["chat"][i]["player_slot"]
    #                         ])

    #                 except KeyError: 
    #                     # pass
    #                     print('에러')
                        
    #                 except ValueError: 
    #                     # pass
    #                     print('에러')