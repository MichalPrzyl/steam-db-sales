import requests
from utils import format_price, color

url = "http://store.steampowered.com/api/featuredcategories/?l=polish"

response = requests.get(url)

with open("output.html", 'w') as file:
    data = response.json()
    print(data.keys())
    print(f"\n==================\n")
    games = data['specials']['items']
    output = []


    for game in games:
        del game['large_capsule_image']
        del game['small_capsule_image']
        del game['windows_available']
        del game['mac_available']
        del game['linux_available']
        del game['streamingvideo_available']
        del game['header_image']
        del game['type']

    print(f"\n===================================\n")
    for game in games:
        print(f"{color('HEADER')}name:{color('ENDC')} {game['name']}, {color('HEADER')}price:{color('ENDC')} {format_price(game['final_price'])}")