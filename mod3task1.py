shopping_list = {
    "Monopolowy": ["piwo", "wino", "whisky"],
    "Żabka": ["ogórki", "śledzie", "cola"]
}

for shop, item in shopping_list.items():
    print("Idę do {} i kupuję tam {}".format(shop, item))
