import requests
import json
# Credentials you get from registering a new application
client_id = 'XXXXXXXXXX'

data = {
  'client_id': client_id,
  'response_type': 'code',
  'redirect_uri': 'http://www.example.com',
  'scope': 'read,watch_lists,publish_messages,publish_watch_lists,follow_users,follow_stocks',
  'prompt': 1
}

# Retrieve list of 30 trending equities
r = requests.get('https://api.stocktwits.com/api/2/trending/symbols/equities.json')
ans = json.loads(r.text)

for i in range(30):
    print(ans['symbols'][i]['symbol'])

# Print message about specific stock:
# Stock at index 0
query = 'https://api.stocktwits.com/api/2/streams/symbol/' + ans['symbols'][0]['symbol'] + '.json'
# print(query)
r = ''
r = requests.get(query)

ans = ''
ans = json.loads(r.text)

for i in range(30):
    print(ans['messages'][i]['body'])
