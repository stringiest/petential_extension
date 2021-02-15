from django.test import TestCase, Client
from .models import generate_unique_code, Pack, Food
from django.utils import timezone
import random
from .serializers import FoodSerializer, CreateFoodSerializer, PackSerializer, CreatePackSerializer, WalkSerializer, CreateWalkSerializer
from importlib import import_module


class ModifySessionMixin(object):
    client = Client()

    def create_session(self):   
        session_engine = import_module(settings.SESSION_ENGINE)       
        print(session_engine) 
        store = session_engine.SessionStore()    
        print(store)                      
        store.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

class PackTest(TestCase):
  
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

class GetPackViewTest(TestCase):

    def test_get_pack_empty_code(self):
        print('******************test_get_pack_empty_code()**********************')
        code_test_data = {}
        # send GET request.
        response = self.client.get(path='/api/get-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Code paramater not found in request"}', response.content)


class JoinPackViewTest(TestCase):

    def create_pack(self, code="ADMINS", host="Admin", pet_name="Admin"):
        return Pack.objects.create(code=code, host=host, pet_name=pet_name, created_at=timezone.now())

    def test_join_pack_use_empty_code(self):
        print('******************test_join_pack_use_empty_code()**********************')
        code_test_data = {}
        # send POST request.
        response = self.client.post(path='/api/join-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Invalid post data, did not find a code key"}', response.content)

    def test_join_pack_use_invalid_code(self):
        print('******************test_join_pack_use_invalid_code()**********************')
        code_test_data = {'code' :'ABCDEF'}
        response = self.client.post(path='/api/join-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        # if the provided string exist in the response content html, then pass.
        self.assertIn(b'{"Bad Request":"Invalid Pack Code"}', response.content)

    def test_join_pack_success(self):
        print('******************test_join_pack_success()**********************')
        pack = self.create_pack()
        code_test_data = {'code' :'ADMINS'}
        response = self.client.post(path='/api/join-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"message":"Pack Joined!"}', response.content)

class CreatePackViewTest(TestCase):

    def test_create_pack_use_empty_date(self):
        print('******************test_create_pack_use_empty_code()**********************')
        code_test_data = {}
        # send POST request.
        response = self.client.post(path='/api/add-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Invalid data..."}', response.content)



class CreateFoodViewTest(ModifySessionMixin, TestCase):
    
    def test_add_food_with_invalid_data(self):
        print('******************test_add_food_with_invalid_data()**********************')
        food_test_data = {}
        # send POST request.
        response = self.client.post(path='/api/add-food', data=food_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Invalid data..."}', response.content)
    
    def test_add_food_success(self):
        print('******************test_add_food_success()**********************')
        self.create_session()
        food_test_data = {'meal_type':'breakfast', 'date':'2021-02-12', 'comment':'yum', 'treats':'4'}
        response = self.client.post(path='/api/add-food', data=food_test_data)
        print('Response status code : ' + str(response.status_code))
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'{"message":"Pack Joined!"}', response.content)

