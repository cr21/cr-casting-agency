import unittest
import os
from app import app,create_app
from database.models import db, Movie, Actor,setup_db, test_db_drop_and_create_all
import json
from datetime import date
import os
# database_path ='postgres://postgres:root@localhost:5432/test_casting'


database_path = os.environ['TEST_DATABASE_URL']
casting_assistant= os.environ['casting_assistant']
casting_director = os.environ['casting_director']
producer = os.environ['producer']

class Casting_TestCase(unittest.TestCase):
    def setUp(self):
        # app=create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = database_path
        self.app = app.test_client()
        test_db_drop_and_create_all()
        # for rule in app.url_map.iter_rules():
        #     print(rule)

        self.actor = {
                        "name":"Kajol",
                        "age":45,
                        "gender": "Female"
                    }
        self.movie = {
                        "title":"Ramleela1",
                        "release_date": date.today(),
                        "actor_id":2
                    }
    def test_get_movies_with_casting_director(self):
        res = self.app.get('/movies',headers={'Authorization':casting_assistant})
        # print(res)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        # self.assertEqual(data['total_record'],4)
    
    def test_get_movies_withoutAuth(self):
        res = self.app.get('/movies')
        print(res.data)
        self.assertEqual(res.status_code,401)


    def test_get_actors_with_casting_director(self):
        res = self.app.get('/actors',headers={'Authorization':casting_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        # self.assertEqual(data['total_record'],4)
    
    def test_get_actors_withoutAuth(self):
        res = self.app.get('/actors')
        print(res)
        self.assertEqual(res.status_code,401)

    def test_create_new_movie(self):
        res = self.app.post('/movies', json=self.movie, headers={'Authorization':producer})
        data = json.loads(res.data)
        # print(data.items)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_create_new_movie_auth_error(self):
        res = self.app.post('/movies', json=self.movie, headers={'Authorization':casting_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_new_Actor(self):
        res = self.app.post('/actors', json=self.actor, headers={'Authorization':casting_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_create_new_actor_auth_error(self):
        res = self.app.post('/actors', json=self.actor, headers={'Authorization':casting_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    
    def test_delete_actors(self):
        res = self.app.delete('/actors/1',headers={'Authorization':casting_director})
        print(res)
        self.assertEqual(res.status_code, 200)
        
    
    def test_patch_movie_success(self):
        res = self.app.patch('/movies/2', 
                                headers={'Authorization': producer}, 
                                json = {"title":"XYZ"}
                            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_patch_movie_Auth_error(self):
        res = self.app.patch('/movies/3', 
                                headers={'Authorization': casting_assistant}, 
                                json = {"title":"XYZ"}
                            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    
    # # delete Failure message 404 error
    def test_404_delete_if_actor_does_not_exist(self):
        res = self.app.delete('/actors/2000',headers={'Authorization':producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_movie_delete_auth_error(self):
        res = self.app.delete('/movies/2000',headers={'Authorization':casting_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)




if __name__ == '__main__':
    unittest.main()