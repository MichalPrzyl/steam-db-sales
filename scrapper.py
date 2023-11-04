import requests
from utils import format_price

# url found in google in 30 secs
url = "http://store.steampowered.com/api/featuredcategories/?l=polish"
response = requests.get(url)

data = response.json()
games = data['specials']['items']

MAX_NAME_LENGTH = max(len(d["name"]) for d in games)  # get the longest name
MAX_PRICE_LENGTH = max(len(str(d["final_price"])) for d in games)  # get the longest price
COLUMN_WIDTH_NAME= MAX_NAME_LENGTH
COLUMN_WIDTH_PRICE = MAX_PRICE_LENGTH + 4
WHOLE_WIDTH = COLUMN_WIDTH_NAME + COLUMN_WIDTH_PRICE + 7

# print headers
print(WHOLE_WIDTH * "=")
print("| {:^{}s} | {:^{}s} |".format("NAME", COLUMN_WIDTH_NAME, "PRICE", COLUMN_WIDTH_PRICE))
print(WHOLE_WIDTH * "=")

# removing unnecesary informations
for game in games:
    del game['large_capsule_image']
    del game['small_capsule_image']
    del game['windows_available']
    del game['mac_available']
    del game['linux_available']
    del game['streamingvideo_available']
    del game['header_image']
    del game['type']
    # actuall printing record (table look-like)
    print("| {:<{}s} | {:>{}s} |".format(
                                        game['name'], 
                                        COLUMN_WIDTH_NAME, 
                                        format_price(game['final_price']) + " zł", 
                                        COLUMN_WIDTH_PRICE))

print(WHOLE_WIDTH * "=")
