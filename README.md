# Udacity_FSND_Capstone_Project
Udacity Full Stack Developer Nanodegree Project Capstone Projects


## Getting Started

### Installing Dependencies

#### Python 3 

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Example in my code :

python3 -m venv env
source env/bin/activate

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies 

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

- [Flask-Migrate] (https://flask-migrate.readthedocs.io/en/latest/) is use for detecting changes in Database and migration of changes in Database.



- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup

Also set the following environmental variable for Auth0

```bash
# You can replace following with your details  This is my details and this token can be useful for running and testing my app, but this token might expired
export DATABASE_URL='postgres://postgres:root@localhost:5432/casting1'
export TEST_DATABASE_URL='postgres://postgres:root@localhost:5432/test_casting'
export AUTH0_DOMAIN='cr-full-stack.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='castingapp'
export casting_assistant='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3NDI0ODkwNjMyNDcyNDI3MTc2IiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTgzMDI3NiwiZXhwIjoxNTg5OTE2Njc2LCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.UtuEEkE-pAklBsh9i4e2rXILKMrR9pa_kdnGtizfde4VvBNSCOzF0nC8sK1Fl4_SKDIe3jrQU8YNJp0sSCBKnYFfQ3k1I3QQnQna2NcB1aA2cykoUEcucy7Gyr8-QLm-_HAeZwh_R3EbbTgMCxw2IMzglvcyIqjcfmMT6F9EwjofW3wDHroUwYFbsyRbe2oM0QxVgQ0lOqqDhiXQe9SbUAxa8QhX6LIYx3piCZqN23nfBOHVmvE_n8O2EJNnYrce6tAyFBhMlhL4LoOkF-AS13fYJ4dQjWC210iGPDrK9Lk0dshP9KrqVr6vqlEd14I1B30H1zf3GLh_-p5lOEM6XQ'
export casting_director='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA5ODkwMDM0OTczMTgyMjM0OTUyIiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTgzMDA2NywiZXhwIjoxNTg5OTE2NDY3LCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.tHPSX2hVtCKm4cIUiBcrvs0VOppIQTlvGpnaw63hm0aJt7V8SCqW1ndKggBYhR-6zBWhTe1UG5laPdejLQ00q9klMHpljUq8tth9XrHQuRFGVoe_xSJloIt191L_u8FL1MA6xZoOU8iK7u4W6-BMMpuVrjzhGwazlmcYaAMfY7ADM_zeh58tIupbP7gtO9W5MZSnhlPN2HPPXftHnW_GB5DLmj8rRF1aehH6wy2QCRrmNlBlprKZpPKRWaw3OH_FAxD_zvck97OtUsxgPVaionAp2D_itfyClwhL5NVwrZBxqOFlegWrnTqXWm-ZQ3o-SK3bWnwq1aPyIOBLgd6sKw'
export producer='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3NDc0MjczMTA5NTc1NDkwMjI5IiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTgyOTkzMSwiZXhwIjoxNTg5OTE2MzMxLCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.MD0nmktiBVti5gMUpzeBz51AMP54AKw6133lws_7nVpAIacXk7kmDcjlOvBXoo24OLSCwZm79PGNHE8Jv9QWBVY1xqs4N5TL0Mu-TUXL3ETzh42r2T8n90oKlDupdVrmRKeE7b2ybuyg9LOvjKddjV_qHeNe4Mw3Kgn8-l2mcbR5BoiwDArmlxJ7iKhLWKHmttShDjaqGdW8dJn9qy3MXo9R2MpKULwiERZTHvpfp0dxzMQQouH1JGmQJySyo79885RRctCpXqbgQdYSlHSg-ZKl5kfCDsA6cW565wlgHhTxmNAJM1WG5F1ASyOXeeGMG1VaOqGI6G3hwjsxa0S2_w'

```

To run the server, execute:
run this in your terminal where code is :  python3 app.py


The `--reload` flag will detect file changes and restart the server automatically.


### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain  # add this in environment variable
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `post:actors`
    - `get:actors`
    - `delete:actors`
    - `patch:actors`
    - `post:movies`
    - `get:movies`
    - `delete:movies`
    - `patch:movies`

6. Create new roles for:
    - Casting Assistant
      - Can view actors and movies

    - Casting Director
        - All permissions a Casting Assistant has and…
        - Add or delete an actor from the database
        - Modify actors or movies

    - Executive Producer
        - All permissions a Casting Director has and…
        - Add or delete a movie from the database

7. Endpoints

    | Functionality            | Endpoint                      | Casting assistant  |  Casting Director  | Executive Producer |
    | ------------------------ | ----------------------------- | :----------------: | :----------------: | :----------------: |
    | Fetches a list of actors | GET /actors                   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
    | Fetches a list of movies | GET /movies                   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
    | Fetches a specific actor | GET /actors/&lt;id&gt;        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
    | Fetches a specific movie | GET /movies/&lt;id&gt;        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
    | Creates an actor         | POST /actor                   |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
    | Fetches Movie actors     | GET /movies/&lt;id&gt;/actors |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
    | Patches an actor         | PATCH /actors/&lt;id&gt;      |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
    | Delete an Actor          | DELETE /actors/&lt;id&gt;     |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
    | Creates a movie          | POST /movies                  |        :x:         |        :x:         | :heavy_check_mark: |
    | Deletes a movie          | DELETE /movies/&lt;id&gt;     |        :x:         |        :x:         | :heavy_check_mark: |

    
8. Test your endpoints with [Postman](https://getpostman.com).

   - Register 3 users - assign the Casting Assistant role to the first,Casting Director to the second and Executive Producer to the third
   - Sign into each account and make note of the JWT.
   - if you change the jwt please add in environment variable
   - Import the postman collection `Casting.postman_collection.json`
   - Right-clicking the collection folder ,select edit and navigate to the variables tab, update the JWT token for the three different roles i.e Casting Assistant, Casting Director and Executive Producer.
   - Run the collection to test the endpoints
   >_tip_: To ensure that the tests run correctly please update the ids for
    resources that require accessing a specific record by id, and make sure you create record and then check

9. Testing with pytest

   - You can also run unit tests by opening your terminal
   - run : python3 test_app.py
