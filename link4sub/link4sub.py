import requests
import base64
import urllib.parse
import re
from urllib.parse import urlparse
import subprocess
import sys
def auto_install(*packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f">> Installing: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            __import__(package)

auto_install("requests")
def match(url):
    if not url.startswith("http"):
        url = "https://" + url
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    match = re.match(r'^([\w\-]+)$', path)
    if match:
        return match.group(1)
    return None

def extract(json):
    encoded_url = json['data']['data']['lnk']['lnk1']['url']
    try:
        decoded_url = urllib.parse.unquote(base64.b64decode(encoded_url).decode('utf-8'))
        return decoded_url
    except Exception as e:
        raise Exception(f'>> Failed to decode URL: {e}')
def f():
    print('>> Vui lòng nhập url gốc dưới dạng "https://link4sub.com/abc123 không phải https://link4sub.com/blog/top-5-game-mobl ,..."')
    url = input('>> Vui lòng nhập url: ')
    scode = match(url)
    response = requests.get(f'https://link4sub.com/stu/{scode}/fetch-data')
    if response.status_code == 200:
        data = response.json()
        try:
            links = extract(data)
            print(f'>> Link đích: {links}')
        except Exception as e:
            print(f'>> Error fetching links: {e}')
    else:
        raise Exception(f">> Failed to fetch data: {response.status_code}")
    
if __name__ == "__main__":
    f()
