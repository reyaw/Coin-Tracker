import requests

ifttt_webhook_url = 'https://maker.ifttt.com/trigger/bepis/with/key/di9LGZrw5TAcILa5deoyzE'
print(requests.post(ifttt_webhook_url))