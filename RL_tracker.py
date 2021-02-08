from requests_html import HTMLSession
import json

# Insert your API_key here
API_key="XXXXXXXXXXX-XXXXX-XXXXXX-XXXXXXXX"

def parse_json(answer):
    answer=answer["data"]
    this_player={}
    this_player["name"]=answer["platformInfo"]["platformUserHandle"]
    for i in range(2,5):
        ranking={}
        ranking["rank"]=answer["segments"][i]["stats"]["tier"]["value"]
        ranking["div"]=answer["segments"][i]["stats"]["division"]["value"]+1
        ranking["MMR"]=answer["segments"][i]["stats"]["rating"]["value"]
        this_player[f'{i-1}v{i-1}']=ranking
    return this_player

#feel free to add more steam ids
steam_ids=['76561198327846028','76561199023677910','76561198446567626'] 
all_players={}
session =HTMLSession()
headers={'TRN-Api-Key':API_key}
for id in steam_ids:
    url= f"https://public-api.tracker.gg/v2/rocket-league/standard/profile/steam/{id}"
    response = session.get(url,headers=headers)
    all_players[id]=parse_json(json.loads(response.text))

print(json.dumps(all_players, indent=4))
