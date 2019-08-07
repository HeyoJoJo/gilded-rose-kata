# -*- coding: utf-8 -*-
import unittest
from mock import patch

from gilded_rose import Item, GildedRose, CommonItem, AgedItem, TicketItem, LegendaryItem, ConjuredItem

class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_decrease_sell_date(self):
        item = Item("clothes of body concealment", 10, 10)
        gilded_rose = GildedRose(item)
        gilded_rose.decrease_sell_date(item)
        self.assertEquals(9, item.sell_in)

    def test_void_quality(self):
        item = Item("unused backstage pass", 0, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.void_quality(item)
        self.assertEquals(0, item.quality)
    
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
    
    def test_add_aged_item_quality_doubles_after_sell_date(self):
        base_item = Item("Aged coca cola classic", -1, 10)
        aged_item = AgedItem(base_item)
        gilded_rose = GildedRose([aged_item])
        gilded_rose.add_quality(aged_item)
        self.assertEquals(12, aged_item.quality)

    def test_remove_quality_default(self):
        items = [Item("Iron Shield", 10, 10)]
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
    
    def test_remove_quality_on_sell_by_date(self):
        item = Item("Apple on the sell by date", 0 , 5)
        gilded_rose = GildedRose([item])
        gilded_rose.decrease_quality(item)
        self.assertEquals(3, item.quality)
    
    def test_remove_quality_on_sell_by_date(self):
        item = Item("Apple after the sell by date", -1 , 3)
        gilded_rose = GildedRose([item])
        gilded_rose.decrease_quality(item)
        self.assertEquals(1, item.quality)

    def test_can_create_common_item(self):
        base_item = Item("Health Potion(medium)", 10, 10)
        items = [CommonItem(base_item)]
        self.assertEquals(CommonItem, items[0].__class__)

    def test_can_create_aged_item(self):
        base_item = Item("Aged Brie", 10, 10)       
        items = [AgedItem(base_item)]
        self.assertEquals(AgedItem, items[0].__class__)

    def test_can_create_ticket_item(self):
        base_item = Item("Backstage passes to DragonForce", 10, 10)
        items = [TicketItem(base_item)]
        self.assertEquals(TicketItem, items[0].__class__)

    def test_can_create_legendary_item(self):
        base_item = Item("Sulfuras Greatsword of Bigness", 10, 30)
        items = [LegendaryItem(base_item)]
        self.assertEquals(LegendaryItem, items[0].__class__)

    def test_legendary_item_value_always_made_80(self):
        base_item = Item("Sulfuras Greatsword of Bigness", 10, 30)
        items = [LegendaryItem(base_item)]
        self.assertEquals(80, items[0].quality)

    def test_inspect_item_can_identify_legendary_item(self):
        item = Item("Sulfuras helmet of cranial blade deflection", 5, 10)
        gilded_rose = GildedRose([item])
        item = gilded_rose.inspect_item(item)
        self.assertEquals(LegendaryItem, item.__class__)

    def test_inspect_item_can_identify_Aged_item(self):
        item = Item("Aged cheese of eating", 5, 10)
        gilded_rose = GildedRose([item])
        item = gilded_rose.inspect_item(item)
        self.assertEquals(AgedItem, item.__class__)

    def test_inspect_item_can_identify_ticket_item(self):
        item = Item("Backstage passes to William of Pump", 10, 10)
        gilded_rose = GildedRose([item])
        item = gilded_rose.inspect_item(item)
        self.assertEquals(TicketItem, item.__class__)
    
    def test_inspect_item_can_identify_conjured_item(self):
        item = Item("Conjured enchanted club of bonking", 10, 10)
        gilded_rose = GildedRose([item])
        item = gilded_rose.inspect_item(item)
        self.assertEquals(ConjuredItem, item.__class__)

    def test_inspect_item_can_identify_common_item(self):
        item = Item("Wyvern wings with buffalo sauce", 10, 10)
        gilded_rose = GildedRose([item])
        item = gilded_rose.inspect_item(item)
        self.assertEquals(CommonItem, item.__class__)
    
    def test_update_quality_should_always_add_quality_to_aged_item(self):
        item = Item("Aged dragon heart", 0, 20)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertGreater(updated_items[0].quality, 20)

    def test_update_quality_should_hit_max_quality_aged_item(self):
        item = Item("Aged dragon heart", -10, 49)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(50, updated_items[0].quality)
    
    def test_update_quality_should_decrease_sell_date(self):
        item = Item("Aged dragon heart", -10, 49)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(-11, updated_items[0].sell_in)

    def test_update_quality_common_item_decrease_quality(self):
        item = Item("Eyepatch of blindness", 10, 5)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(4, updated_items[0].quality)

    def test_update_quality_expired_common_item(self):
        item = Item("Dusty eyepatch of blindness", -1, 1)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(0, updated_items[0].quality)
    
    def test_update_quality_expired_common_item_degrades_faster(self):
        item = Item("Dusty but valuable eyepatch of blindness", -1, 10)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(8, updated_items[0].quality)

    def test_update_quality_new_conjured_item(self):
        item = Item("Conjured broadsword of hurting", 10, 20)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(18, updated_items[0].quality)

    def test_update_quality_expired_conjured_item(self):
        item = Item("Conjured emergency mace", 0, 5)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(1, updated_items[0].quality)

    def test_update_quality_concert_ticket_default(self):
        item = Item("Backstage passes to hatsune miku", 12, 10)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(11, updated_items[0].quality)
        
    def test_update_quality_concert_ticket_ten_days_left(self):
        item = Item("Backstage passes to hatsune miku", 10, 20)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(22, updated_items[0].quality)
    
    def test_update_ticket_five_or_fewer_days_left(self):
        item = Item("Backstage passes but hatsune is a dragon now", 5, 30)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(33, updated_items[0].quality)

    def test_update_expired_ticket(self):
        item = Item("Backstage passes but hatsune is a dragon now", 0, 40)
        gilded_rose = GildedRose([item])
        updated_items = gilded_rose.update_quality()
        self.assertEquals(0, updated_items[0].quality)

if __name__ == '__main__':
    unittest.main()
