from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        item = Item(name="Test Item")
        item.save()
        self.assertEqual(item.name, "Test Item")
        self.assertFalse(item.done)

    def test_can_create_an_item_with_a_name_and_status_is_set_to_done(self):
        item = Item(name="Test Item", done=True)
        item.save()
        self.assertEqual(item.name, "Test Item")
        self.assertTrue(item.done)

    def test_item_as_a_string(self):
        item = Item(name="Test Item")
        self.assertEqual("Test Item", str(item))
