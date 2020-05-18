import unittest
import os
from app import app,create_app
from database.models import db, Movie, Actor,setup_db, db_drop_and_create_all
import json
from datetime import date
import os
# database_path ='postgres://postgres:root@localhost:5432/test_casting'


database_path = os.environ['TEST_DATABASE_URL']
casting_assistant='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3NDI0ODkwNjMyNDcyNDI3MTc2IiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTgzMDI3NiwiZXhwIjoxNTg5OTE2Njc2LCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.UtuEEkE-pAklBsh9i4e2rXILKMrR9pa_kdnGtizfde4VvBNSCOzF0nC8sK1Fl4_SKDIe3jrQU8YNJp0sSCBKnYFfQ3k1I3QQnQna2NcB1aA2cykoUEcucy7Gyr8-QLm-_HAeZwh_R3EbbTgMCxw2IMzglvcyIqjcfmMT6F9EwjofW3wDHroUwYFbsyRbe2oM0QxVgQ0lOqqDhiXQe9SbUAxa8QhX6LIYx3piCZqN23nfBOHVmvE_n8O2EJNnYrce6tAyFBhMlhL4LoOkF-AS13fYJ4dQjWC210iGPDrK9Lk0dshP9KrqVr6vqlEd14I1B30H1zf3GLh_-p5lOEM6XQ'
casting_director = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA5ODkwMDM0OTczMTgyMjM0OTUyIiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTgzMDA2NywiZXhwIjoxNTg5OTE2NDY3LCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.tHPSX2hVtCKm4cIUiBcrvs0VOppIQTlvGpnaw63hm0aJt7V8SCqW1ndKggBYhR-6zBWhTe1UG5laPdejLQ00q9klMHpljUq8tth9XrHQuRFGVoe_xSJloIt191L_u8FL1MA6xZoOU8iK7u4W6-BMMpuVrjzhGwazlmcYaAMfY7ADM_zeh58tIupbP7gtO9W5MZSnhlPN2HPPXftHnW_GB5DLmj8rRF1aehH6wy2QCRrmNlBlprKZpPKRWaw3OH_FAxD_zvck97OtUsxgPVaionAp2D_itfyClwhL5NVwrZBxqOFlegWrnTqXWm-ZQ3o-SK3bWnwq1aPyIOBLgd6sKw'
producer = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3NDc0MjczMTA5NTc1NDkwMjI5IiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTgyOTkzMSwiZXhwIjoxNTg5OTE2MzMxLCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.MD0nmktiBVti5gMUpzeBz51AMP54AKw6133lws_7nVpAIacXk7kmDcjlOvBXoo24OLSCwZm79PGNHE8Jv9QWBVY1xqs4N5TL0Mu-TUXL3ETzh42r2T8n90oKlDupdVrmRKeE7b2ybuyg9LOvjKddjV_qHeNe4Mw3Kgn8-l2mcbR5BoiwDArmlxJ7iKhLWKHmttShDjaqGdW8dJn9qy3MXo9R2MpKULwiERZTHvpfp0dxzMQQouH1JGmQJySyo79885RRctCpXqbgQdYSlHSg-ZKl5kfCDsA6cW565wlgHhTxmNAJM1WG5F1ASyOXeeGMG1VaOqGI6G3hwjsxa0S2_w'

class Casting_TestCase(unittest.TestCase):
    def setUp(self):
        # app=create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = database_path
        self.app = app.test_client()
        db_drop_and_create_all()
        # for rule in app.url_map.iter_rules():
        #     print(rule)

        self.actor = {
                        "name":"Kajol",
                        "age":45,
                        "gender": "Female"
                    }
        self.movie = {
                        "title":"Ramleela",
                        "release_date": date.today(),
                        "actor_id":1
                    }
    def test_get_movies_with_casting_director(self):
        res = self.app.get('/movies',headers={'Authorization':casting_assistant})
        # print(res)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['total_record'],4)
    
    def test_get_movies_withoutAuth(self):
        res = self.app.get('/movies')
        print(res.data)
        self.assertEqual(res.status_code,401)


    def test_get_actors_with_casting_director(self):
        res = self.app.get('/actors',headers={'Authorization':casting_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['total_record'],4)
    
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
        res = self.app.patch('/movies/1', 
                                headers={'Authorization': producer}, 
                                json = {"title":"XYZ"}
                            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_patch_movie_Auth_error(self):
        res = self.app.patch('/movies/1', 
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