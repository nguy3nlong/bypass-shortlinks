import requests
import time
def format_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url + '/'
    return url
def synurl(url, type):
    if type == 'direct':
        headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.6',
        'Connection': 'keep-alive',
        'Origin': url,
        'Referer': url,
        }
        response = requests.get('https://synurl.vip/cd?&t=70', headers=headers)
        if response.status_code == 200:
            time.sleep(75)
            fresponse = requests.get(f'https://synurl.vip/load_traffic?&r=&w={url}&t=70&ti=0', headers=headers)
            if fresponse.status_code == 200:
                code = fresponse.json()['data']['html']
                print(f'Code: {code}')
            else:
                print('Lỗi bước cuối')
        else:
            print('Lỗi, vui lòng báo cáo admin')

if __name__ == '__main__':
    url = format_url(input('Nhập url nhiệm vụ: '))
    synurl(url, 'direct')
