from django.test import TestCase
from .models import Pack
from django.utils import timezone

class PackTest(TestCase):
   # creates a pack object and returns it 
    def create_pack(self, code="ABCDEF", host="Georgie", pet_name="Baloo"):
        return Pack.objects.create(code=code, host=host, pet_name=pet_name, created_at=timezone.now())

# tests to see if the pack object has the properties we expect
    def test_pack_creation(self):
        pack = self.create_pack()
        self.assertTrue(isinstance(pack, Pack))
        self.assertEqual(pack._str_(), pack.code)