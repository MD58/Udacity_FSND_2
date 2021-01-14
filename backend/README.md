# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
##### Restore Database
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```
##### Update Connection String
[`./models.py`](./models.py)

The default value is:
```bash
database_name = "trivia"
database_path = "postgres://{}{}/{}".format('postgres:123456@','localhost:5432', database_name)
```

## Running the server

From within the `backend` directory on Windows Powershell, execute:

```bash
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run
```

## Testing
##### Update Test Connection String
[`./test_flaskr.py`](./test_flaskr.py)

The default value is:
```bash
  self.database_name = "trivia_test"
  self.database_path = "postgres://{}{}/{}".format('postgres:123456@','localhost:5432', self.database_name)
```

##### Run the tests
```
python test_flaskr.py
```
