order = ""
def item_order(order):

    salad = order.count("salad")
    hamburger = order.count("hamburger")
    water = order.count("water")

    return("salad:{} hamburger:{} water:{}".format(salad, hamburger, water))


item_order(order)