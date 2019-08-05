# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def inspect_item(self, item):

        if 'Sulfuras' in item.name:
            print("Legendary gear!")
            return LegendaryItem(item)

        # if 'Backstage' in item.name:
        #     print("Backstage pass to a show!")
        #     return TicketItem(item.name)



    def add_quality(self, item, amount = 1):
        print("adding " + str(amount) + " quality to " + item.name)
        item.quality += amount
        if(item.quality > 50):
            item.quality = 50
        print("quality of " + item.name + " is now " + str(item.quality))

    def decrease_quality(self, item, amount = 1):
        print("decreasing quality of " + item.name + " by " + str(amount))
        item.quality -= amount
        if(item.quality < 0):
            item.quality = 0
        print("quality of " + item.name + " is now " + str(item.quality))

    def update_quality(self):
        # Main event loop
        for item in self.items:
            print(item)
            # determine class to duck type to

            # update according to class
        # TODO: Lots of routing


#### CLASS DECS
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

class LegendaryItem(Item):
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = 80
