import socket
from requests import get
from requests.api import request
import os

os.system('color a')

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
#local_ip = '46.165.230.5'
public_ip = get('https://api.ipify.org').text
#public_ip = '46.165.230.5'

print(f'Hostname: {hostname}')
print(f'Local IP: {local_ip}')

import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
postal = data['postal']
coords = data['loc']
tmz = data['timezone']
print('Public IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nPostal : {7} \nCoordinates : {5} \nTimezone : {6} \nOrg : {0}'.format(org,region,country,city,IP,coords,tmz,postal))


input("Enter to quit.")

