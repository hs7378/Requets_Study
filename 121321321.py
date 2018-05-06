from requests import get

ip = get('https://api.ip.la').text
print('My public IP address is: {}'.format(ip))