import requests

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

# Make a request through the Tor connection
# IP visible through Tor
session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)
# Above should print an IP different than your public IP

# Following prints your normal public IP
print(requests.get("http://httpbin.org/ip").text)

from stem import Signal
from stem.control import Controller

# signal TOR for a new connection
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="JumpingJaguar27")
        controller.signal(Signal.NEWNYM)

renew_connection()
session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)
input()