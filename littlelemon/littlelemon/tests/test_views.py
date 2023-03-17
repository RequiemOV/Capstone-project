from django.test import testcases
from restaurant.views import *
from django.core import serializers

class MenuItemViewTest(testcases):
    def setup(self):
        Menu.objects.create(
            Title='Juce',
            Price=10.99,
            Inventory=5,
        )
        Menu.objects.create(
            Title='Soup',
            Price=8.99,
            Inventory=7,
        )
        Menu.objects.create(
            Title='Pasta',
            Price=15.99,
            Inventory=3,
        )
    
    def test_getall(self):
        menus = Menu.objects.all()
        self.assertEqual(len(menus), 3)
        expected_menus = [
            {'Title': 'Juce', 'Price': '10.99', 'Inventory': '5'},
            {'Title': 'Soup', 'Price': '8.99', 'Inventory': '7'},
            {'Title': 'Pasta', 'Price': '15.99', 'Inventory': '3'},
        ]

        serializer = serializers.serialize('json', menus)
        response = self.client.get('/api/menus/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, serializer)

        for i, menu in enumerate(menus):
            self.assertEqual(menu.Title, expected_menus[i]['Title'])
            self.assertEqual(menu.Price, expected_menus[i]['Price'])
            self.asserEqual(menu.Inventory, expected_menus[i]['Inventory'])