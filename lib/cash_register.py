#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self._all_items = []
        self._all_price = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self._all_price.append(price * quantity)
        for i in range(quantity):
            self._all_items.append(item)

    def apply_discount(self):
        if self.discount != 0:
            self.total = self.total * (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    @property
    def items(self):
        return self._all_items

    def void_last_transaction(self):
        temp = self._all_price.pop()
        self.total -= temp