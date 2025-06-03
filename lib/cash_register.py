#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0.0
    self.items = []
    self.prices = []

  def add_item(self, title, price, qty = 1):
    self.total += price * qty
    for i in range(qty):
      self.items.append(title)
    self.prices.append(price * qty)

  def apply_discount(self, title = '', discount = 0):
    if self.discount == 0:
      print(f'There is no discount to apply.')
    else:
      self.total -= self.discount / 100 * self.total
      print(f'After the discount, the total comes to ${int(self.total)}.')
  
  def void_last_transaction(self):
    if not self.items:
      self.total = 0.0
    else:
      self.total -= self.prices[-1]