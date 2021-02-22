from django.test import TestCase, Client
from .models import generate_unique_code, Pack, Food, Walk
from django.utils import timezone
import random
from .serializers import FoodSerializer, CreateFoodSerializer, PackSerializer, CreatePackSerializer, WalkSerializer, CreateWalkSerializer
from importlib import import_module
from datetime import datetime
from django.contrib.sessions.models import Session
from freezegun import freeze_time
from unittest.mock import MagicMock


# class ModifySessionMixin(object):
#     client = Client()

#     def create_session(self):   
#         session_engine = import_module(settings.SESSION_ENGINE)       
#         print(session_engine) 
#         store = session_engine.SessionStore()    
#         print(store)                      
#         store.save()
#         self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key



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

    def create_pack(self, code="ADMINS", host="Admin", pet_name="Admin"):
        return Pack.objects.create(code=code, host=host, pet_name=pet_name, created_at=timezone.now())

    def test_get_pack_empty_code(self):
        print('******************test_get_pack_empty_code()**********************')
        code_test_data = {}
        # send GET request.
        response = self.client.get(path='/api/get-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Code paramater not found in request"}', response.content)

    def test_get_pack_invalid_code(self):
        print('******************test_get_pack_invalid_code()**********************')
        code_test_data = {'code' :'ABCDEF'}
        response = self.client.get(path='/api/get-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'{"Pack Not Found":"Invalid Pack Code"}', response.content)
    
    @freeze_time("2021-02-14T12:00:01.062952Z")
    def test_get_pack_success(self):
        print('******************test_get_pack_success()**********************')
        pack = self.create_pack()
        code_test_data = {'code' :'ADMINS'}
        response = self.client.get(path='/api/get-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        # queryset = Pack.objects.all()
        # print(queryset)
        # print(pack.id)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"id":3,"code":"ADMINS","host":"Admin","pet_name":"Admin","created_at":"2021-02-14T12:00:01.062952Z","is_host":false}', response.content)


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

    def create_pack(self, code="BADMIN", host="Badmin", pet_name="Badmin"):
        return Pack.objects.create(code=code, host=host, pet_name=pet_name, created_at=timezone.now())


    def test_create_pack_use_empty_date(self):
        print('******************test_create_pack_use_empty_code()**********************')
        code_test_data = {}
        # send POST request.
        response = self.client.post(path='/api/add-pack', data=code_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Invalid data..."}', response.content)

    @freeze_time("2021-02-14T12:00:01.062952Z")
    def test_create_pack_success(self):
        print('******************test_create_pack_success()**********************')
        random.seed(10)
        session = self.client.session
        # need to work out how to stub the session_key
        session.save()
        pack_test_data = {'pet_name':'Badmin'}
        response = self.client.post(path='/api/add-pack', data=pack_test_data)
        print('Response status code : ' + str(response.status_code))
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'{"id":2,"code":"OLPFVV","host":"Badmin","pet_name":"Badmin","created_at":"2021-02-14T12:00:01.062952Z"}', response.content)

class GetFoodViewTest(TestCase):

    def test_get_food_empty_pack_id(self):
        print('******************test_get_food_empty_pack_id()**********************')
        pack_id_test_data = {}
        # send GET request.
        response = self.client.get(path='/api/get-food', data=pack_id_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Pack id paramater not found in request"}', response.content)


class CreateFoodViewTest(TestCase):
    def create_pack(self, code="ADMINS", host="Admin", pet_name="Admin"):
        return Pack.objects.create(code=code, host=host, pet_name=pet_name, created_at=timezone.now())
    
    def test_add_food_with_invalid_data(self):
        print('******************test_add_food_with_invalid_data()**********************')
        food_test_data = {}
        # send POST request.
        response = self.client.post(path='/api/add-food', data=food_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Invalid data..."}', response.content)
    
    @freeze_time("2021-02-14T12:00:01.062952Z")
    def test_add_food_success(self):
        print('******************test_add_food_success()**********************')
        pack = self.create_pack()
        session = self.client.session
        session['pack_id'] = '1'
        session.save()
        food_test_data = {'meal_type':'breakfast', 'date':'2021-02-12', 'comment':'yum', 'treats':'4'}
        response = self.client.post(path='/api/add-food', data=food_test_data)
        print('Response status code : ' + str(response.status_code))
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'{"id":1,"meal_type":"breakfast","date":"2021-02-12","fed_at":"2021-02-14T12:00:01.062952Z","comment":"yum","treats":4,"pack_id":"1"}', response.content)


class CreateWalkViewTest(TestCase):
    def create_pack(self, code="ADMINS", host="Admin", pet_name="Admin"):
        return Pack.objects.create(code=code, host=host, pet_name=pet_name, created_at=timezone.now())
    
    def test_add_walk_with_invalid_data(self):
        print('******************test_add_walk_with_invalid_data()**********************')
        walk_test_data = {}
        # send POST request.
        response = self.client.post(path='/api/add-walk', data=walk_test_data)
        print('Response status code : ' + str(response.status_code))
        #print('Response content : ' + str(response.content))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'{"Bad Request":"Invalid data..."}', response.content)
    
