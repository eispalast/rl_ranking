import json
import operator


def sort_one(my_list, playlist):
    to_be_sorted={}
    for id in my_list:
        if playlist in my_list[id]:
            to_be_sorted[id]=my_list[id][playlist]
            to_be_sorted[id]['name']=my_list[id]['name']
    sorted_list_ids=sorted(to_be_sorted,key=lambda  x: (to_be_sorted[x]['rank'],to_be_sorted[x]['div'],to_be_sorted[x]['MMR']),reverse=True)
    sorted_list=[]
    for id in sorted_list_ids:
        sorted_list.append({id:to_be_sorted[id]})
    
    return({"playlist":playlist,"ranking":sorted_list})


#my_list is a dictionary like {"playerID":{"3v3":{"rank":13,"div":2,"MMR":950},"2v2":{"rank":...},...},"playerID2":...}
def sort_rankings(my_list,playlists=["3v3","2v2","1v1"]):
    results=[]
    for playlist in playlists:
        results.append(sort_one(my_list,playlist))
        print(results)
    return results




