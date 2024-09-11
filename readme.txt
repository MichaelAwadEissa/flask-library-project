

---venv-------
python -m venv venv
for windows :
venv\scripts\activate
for linux:
source venv/bin/activate


----packages----
pip install Flask SQLAlchemy Flask-WTF Flask-Migrate psycopg2-binary




run app:
windows : set FLASK_APP=app:create_app()

linux :
export FLASK_APP=app:create_app()



create db:
pip install psycopg2-binary

psql -U postgres
sudo -i -u postgres
psql


CREATE DATABASE mydatabase;
\q


Install Required Python Libraries:

pip install Flask SQLAlchemy Flask-Migrate psycopg2-binary
