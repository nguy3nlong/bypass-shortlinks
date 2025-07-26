import requests
import re
import time
type = input('Nhập URL nhiệm vụ: ')
if type == 'https://soikeo.uk.com/' or type == 'https://soikeo.uk.com' or type == 'http://soikeo.uk.com/' or type == 'soikeo.uk.com':
    url = 'https://soikeo.uk.com/'
    key = 'u0cLg'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'
if type == 'https://xosodientu.com/' or type == 'https://xosodientu.com' or type == 'http://xosodientu.com/' or type == 'xosodientu.com':
    url = 'https://xosodientu.com/'
    key = 'sdgQhQny'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'
if type == 'https://hutbephotvietphat.vn/hut-be-phot-tai-hoa-binh-uy-tin-gia-re-0947-888-198-bid21.html' or type == 'https://hutbephotvietphat.vn/hut-be-phot-tai-hoa-binh-uy-tin-gia-re-0947-888-198-bid21.html' or type == 'http://hutbephotvietphat.vn/hut-be-phot-tai-hoa-binh-uy-tin-gia-re-0947-888-198-bid21.html' or type == 'hutbephotvietphat.vn/hut-be-phot-tai-hoa-binh-uy-tin-gia-re-0947-888-198-bid21.html':
    url = 'https://hutbephotvietphat.vn/hut-be-phot-tai-hoa-binh-uy-tin-gia-re-0947-888-198-bid21.html'
    key = 'U8022T1'
    path = '/hut-be-phot-tai-hoa-binh-uy-tin-gia-re-0947-888-198-bid21.html'
    hostname = 'https://hutbephotvietphat.vn'
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://fitting.us.com/' or type == 'https://fitting.us.com' or type == 'http://fitting.us.com/' or type == 'fitting.us.com':
    url = 'https://fitting.us.com/'
    key = 'gLaiBZ'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://www.bape-shirt.us.com/' or type == 'https://www.bape-shirt.us.com' or type == 'http://www.bape-shirt.us.com/' or type == 'www.bape-shirt.us.com':
    url = 'https://www.bape-shirt.us.com/'
    key = 'UfeQFHhb'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://ilink.ru.com/' or type == 'https://ilink.ru.com' or type == 'http://ilink.ru.com/' or type == 'ilink.ru.com':
    url = 'https://ilink.ru.com/'
    key = 'z295Z'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://phale.com.vn/' or type == 'https://phale.com.vn' or type == 'http://phale.com.vn/' or type == 'phale.com.vn':
    url = 'https://phale.com.vn/'
    key = 'L3IRi3'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://huo1tong.cn.com/' or type == 'https://huo1tong.cn.com' or type == 'http://huo1tong.cn.com/' or type == 'huo1tong.cn.com':
    url = 'https://huo1tong.cn.com/'
    key = 'kP2ctth'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://surflabs.io/' or type == 'https://surflabs.io' or type == 'http://surflabs.io/' or type == 'surflabs.io':
    url = 'https://surflabs.io/'
    key = 'IVeaFjaL'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://dienlanh61.com/':
    url = 'https://dienlanh61.com/'
    key = 'YjQKK7'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service-v2.js'

if type == 'https://vietanhgroup24h.com/' or type == 'https://vietanhgroup24h.com' or type == 'http://vietanhgroup24h.com/' or type == 'vietanhgroup24h.com':
    url = 'https://vietanhgroup24h.com/'
    key = 'DgCLuxXT'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://congtymoitruongthoatnuocdothi.com/':
    url = 'https://congtymoitruongthoatnuocdothi.com/'
    key = '4BXZypZU'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service-v2.js'

if type == 'https://hanvico.net/chan-long-cuu-hanvico-c21.html/' or type == 'https://hanvico.net/chan-long-cuu-hanvico-c21.html' or type == 'http://hanvico.net/chan-long-cuu-hanvico-c21.html' or type == 'hanvico.net/chan-long-cuu-hanvico-c21.html':
    url = 'https://hanvico.net/chan-long-cuu-hanvico-c21.html/'
    key = 'kQDqEpZ'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://nhakhoadangluu.com.vn/' or type == 'https://nhakhoadangluu.com.vn' or type == 'http://nhakhoadangluu.com.vn/' or type == 'nhakhoadangluu.com.vn':
    url = 'https://nhakhoadangluu.com.vn/'
    key = 'YHJYioH'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://dietmoithanglong.com.vn/' or type == 'https://dietmoithanglong.com.vn' or type == 'http://dietmoithanglong.com.vn/' or type == 'dietmoithanglong.com.vn':
    url = 'https://dietmoithanglong.com.vn/'
    key = 'SOrB0fZ'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://ava8888.net/' or type == 'https://ava8888.net' or type == 'http://ava8888.net/' or type == 'ava8888.net':
    url = 'https://ava8888.net/'
    key = 'jMNteJA'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://www.dichvuchuyennhahanoi.com/' or type == 'https://www.dichvuchuyennhahanoi.com' or type == 'http://www.dichvuchuyennhahanoi.com/' or type == 'www.dichvuchuyennhahanoi.com':
    url = 'https://www.dichvuchuyennhahanoi.com/'
    key = '4Y2g6CP'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://crooto.io/' or type == 'https://crooto.io' or type == 'http://crooto.io/' or type == 'crooto.io':
    url = 'https://crooto.io/'
    key = '9bf8jQ'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://mi88.icu/' or type == 'https://mi88.icu' or type == 'http://mi88.icu/' or type == 'mi88.icu':
    url = 'https://mi88.icu/'
    key = '6J4aqV3'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://roomsake.com/' or type == 'https://roomsake.com' or type == 'http://roomsake.com/' or type == 'roomsake.com':
    url = 'https://roomsake.com/'
    key = 'rGX2z'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://co88.bio/' or type == 'https://co88.bio' or type == 'http://co88.bio/' or type == 'co88.bio':
    url = 'https://co88.bio/'
    key = 'rIlgO'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://andysdenton.com/' or type == 'https://andysdenton.com' or type == 'http://andysdenton.com/' or type == 'andysdenton.com':
    url = 'https://andysdenton.com/'
    key = '9MGMj'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://quartzsitetourism.com/' or type == 'https://quartzsitetourism.com' or type == 'http://quartzsitetourism.com/' or type == 'quartzsitetourism.com':
    url = 'https://quartzsitetourism.com/'
    key = '1S1vPxj'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://brunswickcafe.com/' or type == 'https://brunswickcafe.com' or type == 'http://brunswickcafe.com/' or type == 'brunswickcafe.com':
    url = 'https://brunswickcafe.com/'
    key = 'WEhUQbi'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'

if type == 'https://modulbank.ru.com/' or type == 'https://modulbank.ru.com' or type == 'http://modulbank.ru.com/' or type == 'modulbank.ru.com':
    url = 'https://modulbank.ru.com/'
    key = 'U6iF599D'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'
if type == 'https://88aas.com/' or type == 'https://88aas.com' or type == 'http://88aas.com/' or type == '88aas.com':
    url = 'https://88aas.com/'
    key = 'fJn539c7'
    path = '/'
    hostname = url
    service = 'https://s1.what-on.com/widget/service.js'
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': hostname,
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}

params = {
    'key': key,
}

response = requests.get(service, params=params, headers=headers)
if response.status_code == 200:
    js = response.text

    pattern = r'var\s+(\w+)\s*=\s*(["\'])(.*?)\2\s*;'
    matches = re.findall(pattern, js)

    def decode(s):
        return bytes(s, "utf-8").decode("unicode_escape")

    
    traffic_key = traffic_id = traffic_domain = traffic_session = uuid_name = None

    for name, _, value in matches:
        if name == "traffic_key":
            traffic_key = decode(value)
        elif name == "traffic_id":
            traffic_id = decode(value)
        elif name == "traffic_domain":
            traffic_domain = decode(value)
        elif name == "traffic_session":
            traffic_session = decode(value)
        elif name == "uuid_name":
            uuid_name = decode(value)
    print('Please wait 90 seconds...')
    time.sleep(90)
    params = {
    'code': traffic_id,
    'traffic_session': traffic_session,
    'screen': '1000 x 1000',
    'browser': 'Skibidi',
    'browserVersion': '100',
    'browserMajorVersion': '100',
    'mobile': 'false',
    'os': 'SkibidiOS',
    'osVersion': '5',
    'cookies': 'true',
    'flashVersion': 'no check',
    'lang': 'en-US',
    'client_id': traffic_session,
    'pathname': path,
    'href': url,
    'hostname': hostname,
}
    aresponse = requests.get('https://s1.what-on.com/widget/get_code.html', params=params, headers=headers)
    if aresponse.status_code == 200:
        print(aresponse.json())
    else:
        print('Không thể load JS hoặc request không thành công')
    

    

else:
    raise RuntimeError("Không thể load JS hoặc request không thành công")
