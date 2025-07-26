import base64
import requests
import random
import time
import re
rod = random.randint(100000, 999999)
rad = str(rod)

unix_time = int(time.time())

url = input('Enter quest url: ')
lurl = input('Enter Linktot url: ')
type = input('Enter quest type: (e.g backlink, normal, changecolor): ')
if type == 'normal':
    headers = {
    'origin': url,
    'referer': url,
    'rid': rad,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15',
}

    response = requests.options('https://linktot.net/ping.php', headers=headers)

if type == 'backlink':
    headers = {
    'origin': url,
    'referer': url,
    'rid': rad,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15',
}

    response = requests.options('https://linktot.net/ping_backlink.php', headers=headers)
print('Pending...')
if response.status_code == 200:
    time.sleep(80)
    gheaders = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': url,
        'priority': 'u=1, i',
        'ref': url,
        'referer': url,
        'rid': rad,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15',
    }

    gjson_data = {
        'href': url,
        'hostname': url,
    }

    gresponse = requests.post('https://linktot.net/get-code.php', headers=gheaders, json=gjson_data)
    if gresponse.status_code == 200:
        gjson = gresponse.json()
        enstring = gjson['code']
        K_Dilink = "1ThDrStTr"

        decoded_base64 = base64.b64decode(enstring).decode('utf-8')

        decrypted_string = ""
        for i in range(len(decoded_base64)):
            decrypted_string += chr(ord(decoded_base64[i]) ^ ord(K_Dilink[i % len(K_Dilink)]))

        print("Giải mã được: ", decrypted_string)
    else:
        print('Không thành công')
else:
    print('Không thành công')
