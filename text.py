import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': 'INSERTMOBILENUMBER',
  'message': 'Hello world.  This text was sent from a docker container using python created by Steve Cosner.',
  'key': 'textbelt',
})
print(resp.json())
