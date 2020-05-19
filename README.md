# Udacity_FSND_Capstone_Project
Udacity Full Stack Developer Nanodegree Project Capstone Projects

## Motivation
This is the last project of the Udacity-Full-Stack-Nanodegree Course. It covers following technical topics in a single app:

Database modeling with postgres & sqlalchemy check -> database/models.py

REST API  for CRUD Operations on database with Flask. check -> app.py)

Automated unit testing for test driven development with Unittest (check-> test_app)


Authorization & Role based Authentification with Auth0 (check Auth/auth.py)

Deployment on Heroku 


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

export casting_assistant='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3NDI0ODkwNjMyNDcyNDI3MTc2IiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTg2ODEzOCwiZXhwIjoxNTg5OTU0NTM4LCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.SBDZBdfOE1INC3ydMnnKUR-4bwwcen1hFvgbLxYOJb0pVT8Ltts-FVvtB9R0voplZxT1leUGC3uuWbB_z-eZlt-isuHk_eMvxuVkbV3TSrBiLtZn026puTHAqYeKrUpngNi5JXnmcfnvlu-jz5R0c27uKF9dNoDn5TnbL9P-qef74Qs6wSHPwI_jO5jNzVjZDIxtft7cETmoa70AGx8pYR1kkNbppiwK6ujbeixAh8jBEyP4_W02sXFPg7ogsJlp7jmMiWwmZjHkInp47wEed6sMcR_gLc5hvzaUY--tcNWyG8a50WOPunn39RCMtKazv1vpYImaxy-SG9q2RhHa8g' 
export casting_director='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA5ODkwMDM0OTczMTgyMjM0OTUyIiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTg2NzkyOCwiZXhwIjoxNTg5OTU0MzI4LCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.YILWqgkox7Klr0BWfZvPCK_LtMf97owJHvwxKheVyOlwA0BHNL1durRmFa5TZBaaVdnn9tLJslpRTvii_63l3BvIvAPQ6xlPP6atM71sNzcfVzgj1BoCIEEBdHix5rTc3NiT9r4yju1sycsbiWatFpXpCihAW82sLcmMmtQKQXwZ0UcrJSnELYLg8BXKORPIoBbkn2OtvQHZknZdWdmznI6a7SjEnc9QhXsePvRFkyin91oLb7oibEABQTwdwJ7xAdWRTk2kDg4WfdaQR3gF_uhmARiAY89hxPbBoARZuedzARVE6Aaftqi6ZdW5FRa_yEWPqCwDPuZE5ZUaGpI-sQ'

export producer='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6bUVPcXM0elFydUFMaEFVcDdWWSJ9.eyJpc3MiOiJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3NDc0MjczMTA5NTc1NDkwMjI5IiwiYXVkIjpbImNhc3RpbmdhcHAiLCJodHRwczovL2NyLWZ1bGwtc3RhY2suYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTg2Nzc0NywiZXhwIjoxNTg5OTU0MTQ3LCJhenAiOiJFaE51bHNwOWJMZkloY2ExTDVIRHRwVWNWWjdiVUF5YyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.P2amR3yLd4lCv-5KMLBEIQ8vg9TJQMyCarIGowYyyOM4am54r6hcilTyYm-VIWoBnRHxBYFWvaiFh3PyYQff7hoL16DQVsv-fYbYvrya-i9XxjcuIR2nPNt_6C-nvDxGggkS4efjcqahxTYprr0VhK6b7b_NY-zCMY2xuQwM5khoeeFcviYWxR_7st7w-crrp1rVFH70w2n66IgY5Z11p5K5bnt4ElPh0IIb1On0fmqSZcqUxqwBNM4SGpMTwjkNqP5crBsuhwcUV_y4Ud4Ly82gzlKqXtDOMIYE4QE2LAWMV2G9axuCmWatYpuPwx-M6thpjVi4Q6HReMpUzgmywA'
```

please create database according to setting given or you can cahnge accordingly 

please run if working with new database setting No table

     python3 manage.py db init 
     
     python3 manage.py db migrate
     
     python3 manage.py db upgrade 
     

To run the server, execute: run this in your terminal where code is : python3 app.py


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


REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET ...
POST ...
DELETE ...
 
GET ‘/movies’
- Fetches a List of Movies Available
- Request Arguments: page , for fetching the data for particular page
- Returns: Returns Object with details about movie id, title, release_date and total_record

Sample response format
 {
    "movies": [
        {
            "id": 1,
            "release_date": "Mon, 18 May 2020 00:00:00 GMT",
            "title": "Matthew first Movie"
        },
        {
            "id": 2,
            "release_date": "Mon, 18 May 2020 00:00:00 GMT",
            "title": "Matthew second Movie"
        }
    ],
    "status_code": 200,
    "success": true,
    "total_record": 2
}


GET ‘/actors
- Fetches a List of Actors Available
- Request Arguments: page , for fetching the data for particular page
- Returns: Returns Object with details about movie id, age, gender, name and total_Record

Sample response format
 {
    "actors": [
        {
            "age": 22,
            "gender": "Female",
            "id": 1,
            "name": "Deepika"
        }
    ],
    "status_code": 200,
    "success": true,
    "total_record": 1
}

GET ‘/movies/<int:id>’
- Fetches a List of Movies for particular  id parameter in request
- Request Arguments: page (OPTIONAL) , for fetching the data for particular page
- Returns: Returns Object with details about actor details, id, release_date, title 

-Sample Request Format:

http://0.0.0.0:8080/movies/1/details

-Sample Responseformat:
 {
    "movie": {
        "actor": {
            "age": 25,
            "gender": "Male",
            "id": 1,
            "name": "Matthew"
        },
        "id": 1,
        "release_date": "Mon, 18 May 2020 00:00:00 GMT",
        "title": "Matthew first Movie"
    },
    "status_code": 200,
    "success": true
}


GET ‘/actors/<int:id>’
- Fetches a List of Actors for particular  id parameter in request
- Request Arguments: page (OPTIONAL) , for fetching the data for particular page
- Returns: Returns Object with details about id, age, gender, movie details 

-Sample Request Format:

http://0.0.0.0:8080/actors/1/details

-Sample Responseformat:
{
    "actor": {
        "age": 20,
        "gender": "Male",
        "id": 3,
        "movies": [
            {
                "id": 3,
                "release_date": "Mon, 18 May 2020 00:00:00 GMT",
                "title": "Matthew third Movie"
            },
            {
                "id": 4,
                "release_date": "Mon, 18 May 2020 00:00:00 GMT",
                "title": "Matthew3 third Movie"
            }
        ],
        "name": "1Matthew"
    },
    "status_code": 200,
    "success": true
}


DELETE ‘/movies/<int:id>’
- Delete Movie based on specific Movie id
- Request Arguments: id (Required) -Movie Id
- Returns: object with status_code and success

Sample Request :
  http://0.0.0.0:8080/movies/1

Sample Response :
  {
    "movie_id": 1,
    "status_code": 200,
    "success": true
}


DELETE ‘/actors/<int:id>’
- Delete Actor based on specific Actor id
- Request Arguments: id (Required) -Actor Id
- Returns: object with status_code and success

Sample Request :
  http://0.0.0.0:8080/actors/1

Sample Response :
  {
    "actor_id": 1,
    "status_code": 200,
    "success": true
}

POST '/actors'
- This endpoint is used for creating new actor
 
Request body:
    {
    "name":"Tom ",
    "age":28,
    "gender": "Male"
  }
    Add Authorization : 'Bearer TOKEN'

 
  
Returns:
  
    {
        "actor": {
            "age": 28,
            "gender": "Male",
            "id": 5,
            "name": "Tom "
        },
        "message": "Tom  created",
        "status_code": 200,
        "success": true
    }

POST: /Movies
 

- This endpoint is used for creating new Movie
 http://0.0.0.0:8080/movies
Request body:
    {
    "title":"TOM AND JERRY",
    "release_date": "{{current_timestamp}}",
   "actor_id":1
  }
    Add Authorization : 'Bearer TOKEN'

 
  
Returns:
    {
        "Movie": {
            "id": 5,
            "release_date": "Tue, 19 May 2020 05:47:25 GMT",
            "title": "TOM AND JERRY"
        },
        "message": "TOM AND JERRY created",
        "status_code": 200,
        "success": true
    }


PATCH ‘/movies/<int:id>’
- EDIT  Movie for particular  id parameter in request
- Returns: Returns Object with updated movie record and status code 

-Sample Request Format:
PATCH
http://0.0.0.0:8080/movies/1/
add Authorization Header : 'Bearer Token'
-Sample Responseformat:
 {
    "movie": {
        "id": 1,
        "release_date": "Mon, 18 May 2020 00:00:00 GMT",
        "title": "JERRY"
    },
    "status_code": 200,
    "success": true
}


```
    
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
