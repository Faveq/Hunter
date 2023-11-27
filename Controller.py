from Allegro import Allegro
from Olx import Olx


def run_search(selected_platform=None, item_to_hunt="", blacklist="", min_price=0, max_price=9999, sort_order=0):
    blacklist = blacklist.replace(", ", ",")
    blacklist = blacklist.replace(" ,", ",")
    blacklist = blacklist.replace(" , ", ",")
    match selected_platform:
        case "olx":
            Olx(set(item_to_hunt.split()), set(blacklist.split(",")), min_price, max_price, sort_order).test()

        case "allegro":
            Allegro(set(item_to_hunt.split()), set(blacklist.split(",")), min_price, max_price, sort_order)

