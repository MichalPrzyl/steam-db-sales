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
        print("{:>30s} -- {:>2s}".format((game['name']), "abcdef"))

    print(f"\n===================================\n")
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
