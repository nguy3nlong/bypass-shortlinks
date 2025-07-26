import requests
import time
def x(eurl):
    if 'vinhomesgreencity.org' in eurl:
        hurl = 'https://vinhomesgreencity.org/'
        code = 'wNpeq5Sror'
    if 'thamtututhanglong.vn' in eurl:
        hurl = 'https://thamtututhanglong.vn/dich-vu-tham-tu-ha-noi/'
        code = 'Tz9l0jtEga'
    if 'duhocbluesea.edu.vn' in eurl:
        hurl = 'https://duhocbluesea.edu.vn/'
        code = 'FO2h370lxh'
    if 'viettinexpress.com' in eurl:
        hurl = 'https://viettinexpress.com/dich-vu/gui-hang-di-my/'
        code = 'QoFDwuMBx3'
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': hurl,
    'priority': 'u=1, i',
    'referer': hurl,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    }
    fdata = {
    'code': code,
    'token': '',
    }
    fresponse = requests.post('https://xlink.co/step', headers=fheaders, data=fdata)
    if fresponse.status_code == 200:
        fdata = fresponse.json()
        token = fdata.get('token')
        sheaders = {
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': hurl,
        'priority': 'u=1, i',
        'referer': hurl,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
        }

        sdata = {
        'code': code,
        'token': token,
        }
        sresponse = requests.post('https://xlink.co/countdown', headers=sheaders, data=sdata)
        if sresponse.status_code == 200:
            sdata = sresponse.json()
            stime = int(sdata.get('timer')) + 5 
            print(f'Please wait {stime} seconds...')
            time.sleep(stime)
            theaders = {
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://vinhomesgreencity.org',
            'referer': 'https://vinhomesgreencity.org/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            }

            tdata = {
            'code': code,
            'token': token,
            }
            tresponse = requests.post('https://xlink.co/continue', headers=theaders, data=tdata)
            if tresponse.status_code == 200:
                tdata = tresponse.json()
                fcode = tdata.get('code')
                print(f'Your code is: {fcode}')
    else:
        return('failed')
    
url = input('Enter quest url: ')
x(url)
