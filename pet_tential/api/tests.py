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
        print('******************test_generate_unique_code()**********************')
        # The below random seed will always create the code OLPFVV
        # Tricky to test uniqueness but can test randomness!
        random.seed(10)
        self.assertEqual(generate_unique_code(), "OLPFVV")


class JoinPackViewTest(TestCase):
    def test_join_pack_use_empty_code(self):
        print('******************test_join_pack_use_empty_code()**********************')
        code_test_data = {}
        # send POST request.
        response = self.client.post(path='/api/join-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Invalid post data, did not find a code key"}', response.content)
