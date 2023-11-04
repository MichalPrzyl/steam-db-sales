import requests
from utils import format_price, color


url = "http://store.steampowered.com/api/featuredcategories/?l=polish"
response = requests.get(url)

with open("output.html", 'w') as file:
    data = response.json()
    games = data['specials']['items']
    MAX_NAME_LENGTH = max(len(d["name"]) for d in games)
    MAX_PRICE_LENGTH = max(len(str(d["final_price"])) for d in games)
    COLUMN_WIDTH_NAME= MAX_NAME_LENGTH
    COLUMN_WIDTH_PRICE = MAX_PRICE_LENGTH + 4
    WHOLE_WIDTH = COLUMN_WIDTH_NAME + COLUMN_WIDTH_PRICE + 7

    # print headers
    print(WHOLE_WIDTH * "=")

    print("| {:^{}s} | {:^{}s} |".format("NAME", COLUMN_WIDTH_NAME, "PRICE", COLUMN_WIDTH_PRICE))
    print(WHOLE_WIDTH * "=")
    for game in games:
        del game['large_capsule_image']
        del game['small_capsule_image']
        del game['windows_available']
        del game['mac_available']
        del game['linux_available']
        del game['streamingvideo_available']
        del game['header_image']
        del game['type']
        print("| {:<{}s} | {:>{}s} |".format(
                                            game['name'], 
                                            COLUMN_WIDTH_NAME, 
                                            format_price(game['final_price']) + " zł", 
                                            COLUMN_WIDTH_PRICE))

    print(WHOLE_WIDTH * "=")
    
