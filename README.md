# Summer
‬
### Training Django in summer
A simple CMS with Django and PostgreSQL

### To get started:
- Create virtual environment
`python3 -m venv 'virtual env name'`
and then activate it
`source 'virtual env name'/bin/activate`

- Clone the repository
`git clone https://github.com/peymanslh/summer.git`
 and go to summer directory with `cd summer`

- Install requirement packages
`pip install -r requirements.txt`

- Create a PostgreSQL database and edit `DATABASE` variable in `summer/settings.py`.

- Run `python manage.py migrate`.

- Create a superuser
`python manage.py createsuperuser`

- Compile .mo files
`python manage.py compilemessages`

- Copy static files `python manage.py collectstatic`

- Run server `python manage.py runserver` and open `localhost:8000` in your browser.
