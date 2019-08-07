# -*- coding: utf-8 -*-
"""Docstring so that pylint stops whining"""

class GildedRose(object):
    """An inn where we sell stuff!"""

    def __init__(self, items):
        self.items = items

    def inspect_item(self, item):
        """Inspects an item and assigns a class to it
        useful for determining behavior further on
        since I can't modify Gob's class [eyeroll emoji]
        It's basically just the adapter pattern."""

        if 'Sulfuras' in item.name:
            return LegendaryItem(item)
        if 'Aged' in item.name:
            return AgedItem(item)
        if 'Backstage' in item.name:
            return TicketItem(item)
        if 'Conjured' in item.name:
            return ConjuredItem(item)
        else:
            return CommonItem(item)


    def add_quality(self, item, amount=1):
        """ Adds quality to an item, unless it is at max
        value of 50 already. Default amount is 1."""

        double = (item.sell_in <= 0) & (item.__class__ == AgedItem)

        if double:
            amount = amount * 2

        item.quality += amount
        if item.quality > 50:
            item.quality = 50

    def decrease_quality(self, item, amount=1):
        """Decreases quality, unless it is already at zero.
        Default amount is 1."""

        double = item.sell_in <= 0
        if double:
            amount = amount * 2
        item.quality -= amount

        if item.quality < 0:
            item.quality = 0

    def decrease_sell_date(self, item):
        """Decreases sell date of an item by 1.
        Do not extend! Time magic is illegal!"""

        item.sell_in -= 1

    def void_quality(self, item):
        """Sets the quality of an item to zero."""

        item.quality = 0

    def update_quality(self):
        """Basically the main event loop,
        inspects all items in self.items and
        updates quality and sell by date."""

        if self.items[0].__class__ == Item:
            new_list = []
            for item in self.items:
                item = self.inspect_item(item)
                new_list.append(item)
            self.items = new_list

        # Main event loop
        for item in self.items:

            if item.__class__ == AgedItem:
                self.add_quality(item)
                self.decrease_sell_date(item)

            if item.__class__ == CommonItem:
                self.decrease_quality(item)
                self.decrease_sell_date(item)

            if item.__class__ == TicketItem:
                self.decrease_sell_date(item)

                if item.sell_in <= 0:
                    self.void_quality(item)

                elif item.sell_in <= 5:
                    self.add_quality(item, 3)

                elif item.sell_in <= 10:
                    self.add_quality(item, 2)

                else:
                    self.add_quality(item)


            if item.__class__ == ConjuredItem:
                self.decrease_quality(item, 2)
                self.decrease_sell_date(item)

            if item.__class__ == LegendaryItem:
                pass

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
    """It extends el goblinos Item class.
    I don't know what else to tell you."""
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality

class AgedItem(Item):
    """Woulda been a lot simpler if he helped out..."""
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality

class ConjuredItem(Item):
    """He knows I'm literally a knight right???"""
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality

class TicketItem(Item):
    """Cruisin for a bruisin, he is... - Yoda"""
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality

class LegendaryItem(Item):
    """...Prayin' for a slayin'..."""
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = 80
