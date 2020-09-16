shopping_list = {
    "Monopolowy": ["piwo", "wino", "whisky"],
    "Żabka": ["ogórki", "śledzie", "cola"]
}

for shop, item in shopping_list.items():
    items = ', '.join(article for article in item)
    print("Idę do {} i kupuję tam {}".format(shop.upper(), items.upper()))
