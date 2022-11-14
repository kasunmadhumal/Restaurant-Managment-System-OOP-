from datetime import date


class OrderItem:

    def __init__(self, item_id, name, price,type_of_order):
        self.item_id = item_id
        self.date = date.today()
        self.type_of_order = type_of_order
        self.name = name
        self.price = price

    def get_item_id(self):
        return self.item_id

    def get_name_id(self):
        return self.name

    def get_price(self):
        return self.price

    def get_date(self):
        return self.date

    def get_type_of_order(self):
        return self.type_of_order
