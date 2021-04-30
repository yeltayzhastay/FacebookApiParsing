import facebook    #sudo pip install facebook-sdk
import itertools
import json
import re
import requests

# https://api.instagram.com/v1/tags/{z.y.yeltay}/media/recent?access_token={EAACQVp4GFvsBAES3i8Aroh5q18BB8Q2hf2bARB5HwylirpdZCjmc9j7Nmsv89fIOtN1vFvEH99vQvsHyaIDKXffGE4khVFrfurzy7mxnQturAEbGRymee2JSLDnVsF2DymNmr60ZAcUpVSjoHhhFZAfZAbZBMxXwuF4nsmbZADhzLqHNPdqBBFzDLBT10Yok2E92IWcR8lnNjcOrEbH5fZC}

access_token = "EAAC43e1D9k8BAIJEvMZBilVY8V1qZALGZAU87wwmGgYarVbv9swJimu2dtUZAItqWXpE8oeEnZABu3eIBQmRbuD5JvJqulCpRTWJAsBR0gBibLdGdyIPttEJS1rKZBVrfyq06WIa8v5MsbWjn5sXqF7xE0UbXOiKmtNZCSGt5DA7QZDZD"
user = "1849247698620787"

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)

# query_string = 'posts?fields=likes,id,created_time,message,story,comments&limit={0}'.format(100)

query_string = 'feed?fields=likes,id,created_time,message,story,comments&limit={0}'.format(100)
posts = graph.get_connections(profile['id'], query_string)

Jstr = json.dumps(posts)
JDict = json.loads(Jstr)

print(JDict['paging'])

posts = []

for i in JDict['data']:
    allID = i['id']
    try:
        allComments = i['comments']

        for a in allComments['data']:  
            
    except:
        pass
