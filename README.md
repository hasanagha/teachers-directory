# Teachers Directory APP

## Installation

Create a virtual environment as required to run django applications
```js   
virtualenv td_env
```
Activate Virtual environment
```js
source td_env/bin/activate
```

Install requirements from the included requirements.txt file
```js
pip install -r requirements.txt
```

Once all the requirements are installed, run the server

```js
python manage.py runserver
```
`Please note, manage.py is on the root of project. Before running the above command, make sure you're on the root.`

## Usage
To add/edit teachers, go to 
`http://localhost:8000/admin`
`username: admin`
`password: admin`

To import teachers:
`http://localhost:8000/import/`

To view list of teachers:
`http://localhost:8000`


## Technical Babble

Uses `Django 3.0.7`.
DB `SQLite3`
