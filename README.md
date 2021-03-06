# postgres_permissions

## What does it do?
This program utilizes a postgres database to store information about blog posts. You can log in and add your own blog posts. Permissions have been set to not allow someone to edit another person's post.

## What languages/libraries/resources does this use?
Python, AWS, Django REST Framework, Docker, ElephantSQL, psycopg2, SimpleJWT, httpie, gunicorn, and whitenoise.

## How do I install and use this?

In your terminal:
```
git clone git@github.com:PyDrummer/postgres_permissions.git

cd postgres_permissions

poetry install

poetry shell

docker-compose up --build

docker-compose down

docker-compose up -d

docker-compose run web python manage.py migrate

docker-compose run web python manage.py createsuperuser
```

Navigate to this URL:

http://127.0.0.1:8000/admin

Now you should be able to sign into your account.

After signing in go to:

http://127.0.0.1:8000/api/v1/blogs/

Now you can add or access the currently stored JSON data.

If you'd like to see the live site:

http://ec2-18-191-160-143.us-east-2.compute.amazonaws.com:8000/admin/

## VERSIONS

1.0: DRF, docker and Postgresql created. Permissions and Serializer created.

1.1: Persistance with the Postgresql DB. New authentification classes added. New depencencies added: SimpleJWT, httpie, gunicorn, and whitenoise.

1.2: Added .env

1.2: ElephantSQL implemented as my db, cors dependency added. AWS hosting implemented.
