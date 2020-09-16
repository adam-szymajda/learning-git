shopping_list = {
    "Monopolowy": ["piwo", "wino", "whisky"],
    "Żabka": ["ogórki", "śledzie", "cola"]
}

counter = 0

for shop, item in shopping_list.items():
    items = ', '.join(article for article in item)
    print("Idę do {} i kupuję tam {}".format(shop.upper(), items.upper()))

for key in shopping_list:
    counter += len(shopping_list[key])

print("W sumie kupuję {} produktów".format(counter))
