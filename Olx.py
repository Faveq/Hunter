def get_sort_order_link(sort_order):
    sort_order_link = '?search%5Border%5D=relevance:desc'
    match sort_order:
        case 1:
            sort_order_link = '?search%5Border%5D=filter_float_price:desc'
        case 2:
            sort_order_link = '?search%5Border%5D=filter_float_price:asc'
        case 3:
            sort_order_link = '?search%5Border%5D=created_at:desc'
    return sort_order_link


class Olx:
    base_link = 'https://www.olx.pl/'

    def __init__(self, item_to_hunt, blacklist, min_price, max_price, sort_order):
        self.item_to_hunt = item_to_hunt
        self.blacklist = blacklist
        self.min_price = min_price
        self.max_price = max_price
        self.sort_order = sort_order


