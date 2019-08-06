# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def inspect_item(self, item):

        if 'Sulfuras' in item.name:
            print("Legendary gear!")
            return LegendaryItem(item)
        
        if 'Aged' in item.name:
            print("Aged Item!")
            return AgedItem(item)

        if 'Backstage' in item.name:
            print("Backstage pass to a show!")
            return TicketItem(item)

        if 'Conjured' in item.name:
            print("Conjured Item!")
            return ConjuredItem(item)
        
        else:
            return CommonItem(item)


    def add_quality(self, item, amount = 1):
        double = (item.sell_in <= 0) & (item.__class__ == AgedItem)
        
        if(double):
            amount = amount * 2

        item.quality += amount
        if(item.quality > 50):
            item.quality = 50

    def decrease_quality(self, item, amount = 1):
        double = item.sell_in <= 0
        if(double):
            amount = amount * 2
        item.quality -= amount

        if(item.quality < 0):
            item.quality = 0
    
    def decrease_sell_date(self, item):
        print("one less day to sell " + item.name)
        item.sell_in -= 1
    
    def void_quality(self, item):
        print("This sat for too long!!!")
        item.quality = 0

    def update_quality(self):
        # See if we've already identified item types
        if(self.items[0].__class__ == Item):
            new_list = []
            for item in self.items:
                item = self.inspect_item(item)
                print("item typed")
                print(item.__class__)
                new_list.append(item)
            self.items = new_list

        # Main event loop
        print(self.items)
        for item in self.items:

            if(item.__class__ == AgedItem):
                self.add_quality(item)
                self.decrease_sell_date(item)

            if(item.__class__ == CommonItem):
                self.decrease_quality(item)
                self.decrease_sell_date(item)

            if(item.__class__ == TicketItem):
                print('we will do something with Ticket items eventually')

            if(item.__class__ == ConjuredItem):
                self.decrease_quality(item, 2)
                self.decrease_sell_date(item)

            if(item.__class__ == LegendaryItem):
                print('Items of this exalted status require no book keeping')
            
            print(self.items)

        return self.items


#### CLASS DECS
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class CommonItem(Item):
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality

class AgedItem(Item):
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality

class ConjuredItem(Item):
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality

class TicketItem(Item):
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality

class LegendaryItem(Item):
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = 80
