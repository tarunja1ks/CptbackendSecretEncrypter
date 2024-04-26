import requests
import json
class generate:
    
    def __init__(self):
        global url
        url = "https://api.random.org/json-rpc/4/invoke"
    def getrandom(self, amount):
        payload = json.dumps({
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "8b38ddfb-4f2b-4145-b8f3-0712c63a67ce",
            "n": amount,
            "min": 1,
            "max": 26
        },
        "id": 1
        })
        headers = {
        'Content-Type': 'application/json',
        'jsonrpc': '2.0',
        'method': 'generateIntegers',
        'params': '[object Object]',
        'id': '1',
        'Cookie': 'RDOSESSION=sm4h31thm5vv5j4afe2if81hi6; csrfToken=df91383eefe869664a47f374754278c8; __cflb=02DiuEMAZFhhWAbaKrF1fuSZexDk78ueybY4Jd5a5Z2YT'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        readvalue=json.loads(response.text)
        print(readvalue['result']['random']['data'])
        
        
        return readvalue['result']['random']['data']