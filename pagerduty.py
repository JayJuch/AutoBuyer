import requests

def sendPagerDutyAlert():
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
        'Authorization': "Token token=sX6mPbPHy65yGwsqvG4w"
    }
    resp = requests.post('https://api.pagerduty.com/incidents', pdbody, headers=pdheaders)
    print(resp)

