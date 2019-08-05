# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, CommonItem, AgedItem, TicketItem, LegendaryItem

class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
    
    def test_add_quality_default(self):
        items = [Item("Potion of speed plus 1", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.add_quality(items[0])
        self.assertEquals(1, items[0].quality)

    def test_add_quality_by_non_default_amount(self):
        items = [Item("Mithril Helm plus 5", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.add_quality(items[0], 5)
        self.assertEquals(5, items[0].quality)

    def test_add_quality_cannot_exceed_50(self):
        items = [Item("Very valuable mace", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.add_quality(items[0], 500)
        self.assertEquals(50, items[0].quality)

    def test_remove_quality_default(self):
        items = [Item("Iron Shield", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.decrease_quality(items[0])
        self.assertEquals(9, items[0].quality)

    def test_remove_quality_non_default_amount(self):
        items = [Item("Almost rotten apple", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.decrease_quality(items[0], 5)
        self.assertEquals(5, items[0].quality)

    def test_remove_quality_non_default_amount(self):
        items = [Item("Completely rotten apple", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.decrease_quality(items[0], 50)
        self.assertEquals(0, items[0].quality)

    def test_can_create_common_item(self):
        items = [CommonItem("Health Potion(medium)", 10, 10)]
        self.assertEquals(CommonItem, items[0].__class__)

    def test_can_create_aged_item(self):        
        items = [AgedItem("Aged Brie", 10, 10)]
        self.assertEquals(AgedItem, items[0].__class__)

    def test_can_create_ticket_item(self):
        items = [TicketItem("Backstage passes to DragonForce", 10, 10)]
        self.assertEquals(TicketItem, items[0].__class__)

    def test_can_create_legendary_item(self):
        base_item = Item("Sulfuras Greatsword of Bigness", 10, 30)
        items = [LegendaryItem(base_item)]
        self.assertEquals(LegendaryItem, items[0].__class__)

    def test_inspect_item_can_identify_legendary_item(self):
        item = Item("Sulfuras helmet of cranial blade deflection", 5, 10)
        gilded_rose = GildedRose([item])
        item = gilded_rose.inspect_item(item)
        print(item)
        print("testMarker")
        self.assertEquals(LegendaryItem, item.__class__)

if __name__ == '__main__':
    unittest.main()
