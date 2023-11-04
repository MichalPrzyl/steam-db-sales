import requests
from utils import format_price, color

COLUMN_WIDTH = 30


url = "http://store.steampowered.com/api/featuredcategories/?l=polish"

response = requests.get(url)

with open("output.html", 'w') as file:
    data = response.json()
    print(data.keys())
    print(f"\n==================\n")
    games = data['specials']['items']
    output = []

    print("| {:<50s} | {:<50s} |".format("NAME", "PRICE"))
    print(60 *"-")
    for game in games:
        del game['large_capsule_image']
        del game['small_capsule_image']
        del game['windows_available']
        del game['mac_available']
        del game['linux_available']
        del game['streamingvideo_available']
        del game['header_image']
        del game['type']
        print("| {:50s} | {:>7s}".format((game['name']), format_price(game['final_price'])))

    print(f"\n===================================\n")
