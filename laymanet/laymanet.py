import requests
import random
import sys


rod = random.randint(100000, 999999)
rad = str(rod)
eurl = input('Nhập url nhiệm vụ: ')
platform = input('Nhập platform (vd: facebook, google): ')
def g(eurl, platform):
    if platform == 'facebook' or platform == 'fb' or platform == 'meta' or platform == 'Facebook':
        platform = 'facebook'
    if platform == 'google' or platform == 'gg' or platform == 'g' or platform == 'Google':
        platform = 'google'
    if eurl == 'https://bamivapharma.com/' or eurl == 'https://bamivapharma.com' or eurl == 'http://bamivapharma.com/' or eurl == 'bamivapharma.com':
        hurl = 'https://bamivapharma.com/'
        code = 'e9VJokISt'
    if eurl == 'https://suamatzenmilk.com/' or eurl == 'https://suamatzenmilk.com' or eurl == 'http://suamatzenmilk.com/' or eurl == 'suamatzenmilk.com':
        hurl = 'https://suamatzenmilk.com/'
        code = 'viyjUHvaj'
    if eurl == 'https://china-airline.net/' or eurl == 'https://china-airline.net' or eurl == 'http://china-airline.net/' or eurl == 'http://china-airline.net' or eurl == 'china-airline.net':
        hurl = 'https://enzymevietnam.com/'
        code = 'oTedsZr2m'
    if eurl == 'https://scarmagic-gm.com/' or eurl == 'https://scarmagic-gm.com' or eurl == 'http://scarmagic-gm.com/' or eurl == 'scarmagic-gm.com':
        hurl = 'https://bamivapharma.com/'
        code = 'e9VJokISt'
    headers = {
        'Host': 'layma.net',
        'Accept-Language': 'en-GB,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
        'Referer': hurl,
        'Connection': 'keep-alive',
    }

    response = requests.get(f'https://layma.net/Traffic/Index/e9VJokISt', headers=headers)
    if response.status_code == 200:
        sheaders = {
            'Host': 'api.layma.net',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            'Accept': '*/*',
            'Origin': hurl,
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': hurl,
            'Priority': 'u=1, i',
        }
        sparams = {
            'keytoken': code,
            'flatform': platform,
        }
        sresponse = response = requests.get('https://api.layma.net/api/admin/campain', params=sparams, headers=sheaders)
        if sresponse.status_code != 200:
            print('Lỗi khi lấy data, vui lòng báo cáo admin')
            sys.exit()
        html = sresponse.json()
        theaders = {
            'Host': 'api.layma.net',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            'Accept': '*/*',
            'Origin': hurl,
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': hurl,
            'Priority': 'u=1, i',
        }

        tjson_data = {
            'uuid': rad,
            'browser': 'Chrome',
            'browserVersion': '100',
            'browserMajorVersion': 100,
            'cookies': True,
            'mobile': False,
            'os': 'OS',
            'osVersion': '5',
            'screen': '1000 x 1000',
            'referrer': hurl,
            'trafficid': html['id'],
            'solution': '1',
        }

        tresponse = requests.post('https://api.layma.net/api/admin/codemanager/getcode', headers=theaders, json=tjson_data)
        if tresponse.status_code == 200:
            th = tresponse.json()
            print(f'Mã: {th['html']}')
        else:
            print('Lỗi khi lấy data, vui lòng báo cáo admin')
    else:
        print('Lỗi khi lấy data, vui lòng báo cáo admin')

if __name__ == '__main__':
    g(eurl, platform)
