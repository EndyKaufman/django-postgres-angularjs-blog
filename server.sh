source venv/bin/activate
export $(cat .env)
gunicorn project.wsgi -b 0.0.0.0:5000