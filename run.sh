source venv/bin/activate
export $(cat .env)
cd front
gulp build --env development
cd ../
python manage.py collectstatic --noinput
gunicorn project.wsgi -b 0.0.0.0:5000