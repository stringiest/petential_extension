from django.test import TestCase
from .models import generate_unique_code, Pack
from django.utils import timezone
import random

class PackTest(TestCase):
   # creates a pack object and returns it 
    # def create_pack(self, code="ABCDEF", host="Georgie", pet_name="Baloo"):
    #     return Pack.objects.create(code=code, host=host, pet_name=pet_name, created_at=timezone.now())

# tests to see if the pack object has the properties we expect
    # def test_pack_creation(self):
    #     pack = self.create_pack()
    #     self.assertTrue(isinstance(pack, Pack))
    #     self.assertEqual(pack._str_(), pack.code)
    
    def test_generate_unique_code(self):
        # The below random seed will always create the code OLPFVV
        # Tricky to test uniqueness but can test randomness!
        random.seed(10)
        self.assertEqual(generate_unique_code(), "OLPFVV")



