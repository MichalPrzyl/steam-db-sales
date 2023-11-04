
elements = [
    {
        'name': "Hello123123123",
        "price": '33,23 zł'
    },
    {
        'name': "second",
        "price": '554,22 zł'
    },
    {
        'name': "lol3",
        "price": '672,91 zł'
    },
]

najdluzszy_name_length = max(len(d["name"]) for d in elements)
WIDTH_VARIABLE = najdluzszy_name_length

# print("| {{:<{}s}} | {:<50s} |".format(WIDTH_VARIABLE).format("NAME", "PRICE"))
# print(60 *"-")


# print("| {{:<{}s}} | {:6.2f} |".format(WIDTH_VARIABLE).format("Bill", "123"))
# print("| {{:<{}s}} | {:6.2f} |".format(WIDTH_VARIABLE).format("Bill", "semanko"))
for game in elements:
    print("| {:<{}s} | {:<{}s} |".format(game['name'], WIDTH_VARIABLE, game['price'], WIDTH_VARIABLE))
    # print("| {:<10s} | {:>7s}".format((game['name']), game['price']))

print(f"\n===================================\n")
