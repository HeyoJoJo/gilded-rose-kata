# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def add_quality(self, item, amount = 1):
        print("adding " + str(amount) + " quality to " + item.name)
        item.quality += amount
        if(item.quality > 50):
            item.quality = 50

    def decrease_quality(self, item, amount = 1):
        print("decreasing quality of " + item.name + " by " + str(amount))
        item.quality -= amount

    def update_quality(self):
        # Main event loop
        for item in self.items:
            print(item)
        # TODO: Lots of routing
            
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class CommonItem(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

class AgedItem(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

class TicketItem(AgedItem):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
