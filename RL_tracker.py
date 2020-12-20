from requests_html import HTMLSession
import json

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
for id in steam_ids:
    url= f"https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/{id}/"
    response = session.get(url)
    response.html.render()
    all_players[id]=parse_json(json.loads(response.html.html.split("\">",1)[1].split("</pre>",1)[0]))

print(json.dumps(all_players, indent=4))
