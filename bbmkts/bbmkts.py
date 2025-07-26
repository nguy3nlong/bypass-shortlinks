from urllib.parse import urlparse
import base64, ast
import re
import urllib.parse
import sys
import time
import subprocess

def install(*packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            __import__(package)

install("requests")

import requests

def extract_domain(url):
    parsed = urlparse(url)
    return parsed.netloc 

def format_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url + '/'
    return url
def simplify_url(url: str) -> str:
    try:
        parsed = urlparse(url if url.startswith(('http://', 'https://')) else 'http://' + url)
        hostname = parsed.hostname or ''
        simplified = hostname.replace('www.', '')
        return simplified
    except Exception:
        return url 
def b():
    url = input('Enter bbmkts url: ')
    regex = re.compile(
        r"https:\/\/bbmkts\.com\/client\/check-client-visit\?id=\d+&linkId=\d+"
    )
    

    while True:
        try:
            response = requests.get(url, timeout=5)
            html = response.text
            matches = regex.findall(html)

            if matches:
                break  

            print("Chưa tìm thấy link, thử lại sau 1s...")
            time.sleep(1)

        except Exception as e:
            print(f"Lỗi khi request: {e}. Đợi 1s rồi thử lại.")
            time.sleep(1)

    try:
        fresponse = requests.get(matches[0], timeout=5)
        data = fresponse.json()

        curl = data.get("url", "")
        pattern = r"https%3A%2F%2F[^\s\"']+"
        cmatches = re.findall(pattern, curl)

        if cmatches:
            decoded_url = urllib.parse.unquote(cmatches[0])
            print(f'Url đích: {decoded_url}')
        else:
            print("Không tìm thấy URL encode trong phản hồi.")
    
    except Exception as e:
        print(f"Lỗi: {e}")
def a():
    url = input('Enter quest url: ')
    furl = format_url(url)
    surl = extract_domain(furl)
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': furl,
    'Referer': furl,
    }
    response = requests.get(
    f'https://bbmkts.com/00abx?00xz={surl}&0012={furl}',
    headers=headers,
    )
    encoded = response.json()['token']
    decoded_str = ast.literal_eval(base64.b64decode(encoded).decode('utf-8'))
    print(f"Mã đã giải: {decoded_str['code']}")

print('''   
[1] Bypass nút (cho nhiệm vụ ấn nút và chờ)
[2] Bypass visit (cho nhiệm vụ phải vào link)
''')
type = input('Chọn loại method bypass (vd: 1, 2): ')
if '1' in type:
    a()
elif '2' in type:
    b()
else:
    print('Vui lòng lựa chọn đúng method')
    sys.exit()
