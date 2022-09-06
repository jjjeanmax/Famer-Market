# Famer-Market

# Requirement:

- Database: PostgreSQL 10.0 or higher.
- Programming language: Python 3.8 or higher.
- Python libraries: Django 4.1 or higher, Django REST Framework 3.12 or higher,
  psycopg2 2.8 or higher.


## Configuration file
When deploying, copy the `configs.json.example` file to the `configs.json` file in the directory
`Famer-Market/famerMarket/famerMarket`.

Example `configs.json` file `Famer-Market/famerMarket/famerMarket/configs.json.example`.

## Start

1. Create and activate virtual environment:

    `python -m venv venv`

2. Install packages:

    `pip install -r requirements.txt`

3. Run migrations:

    `python manage.py migrate`

4. Create superuser:

    `python manage.py createsuperuser`

4. Create config file:

    `configs.json`

6. Export Csv File to Database:
   `$ cd /Famer-Market/famerMarket/famerMarket` and 
    `$ python record.py`

7. Start django server:
    
    `$ python manage.py runserver`
