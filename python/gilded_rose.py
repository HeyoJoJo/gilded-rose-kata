# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def add_quality(self, item, amount = 1):
        print("adding quality to " + item.name)
        item.quality += amount


    def update_quality(self):
        for item in self.items:
            print(item)
            
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
