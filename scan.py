import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def scanForThreats(scanurl):
    api_key = os.getenv("key")
    url = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}'
    data = {
        "client": {
            "clientId":      "ShieldedSurf"
        },
        "threatInfo": {
            "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING", "THREAT_TYPE_UNSPECIFIED"],
            "platformTypes":    ["WINDOWS"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": scanurl}
            ]
        }
    }
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data)
    return response.json()


print(scanForThreats("http://malware.testing.google.test/testing/malware/"))