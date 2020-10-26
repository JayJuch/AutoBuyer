import requests
import os

pdbody = '''
{
  "incident": {
    "type": "incident",
    "title": "test1",
    "service": {
      "id": "P08M1RK",
      "type": "service_reference"
    }
  }
}
'''
pdheaders = {
    "Content-Type": "application/json",
    'Accept': 'application/vnd.pagerduty+json;version=2',
    'From': 'jay.juch@gmail.com',
    'Authorization': "Token token=" + os.environ['PAGERDUTY_APIKEY']
}

def sendPagerDutyAlert():
    resp = requests.post('https://api.pagerduty.com/incidents', pdbody, headers=pdheaders)
    print(resp)

