# django-postgres-angularjs-blog
  Simple blog written on django + angularjs and use postgre sql as database

https://django-postgres-angularjs-blog.herokuapp.com

[![Build Status](https://travis-ci.org/EndyKaufman/django-postgres-angularjs-blog.svg?branch=master)](https://travis-ci.org/EndyKaufman/django-postgres-angularjs-blog)
[![Requirements Status](https://requires.io/github/EndyKaufman/django-postgres-angularjs-blog/requirements.svg?branch=master)](https://requires.io/github/EndyKaufman/django-postgres-angularjs-blog/requirements/?branch=master)

## current progress of project

1. ~~Write function tests work on Protractor + Selenium with PhantomJS~~
2. ~~Move to Vagrant~~
3. ~~Make templates and tests for basic edit mode~~
4. ~~Add test database on sqlite and move it mock data from tests~~
5. ~~Make all methods and classes for authorization~~
6. ~~Move frontend code to submodule~~
7. ~~Migrate production to Postres SQL~~
8. ~~Add Travis CI build~~
8. ~~Add themes support~~
10. ~~Change standard bootstrap theme to beautiful and clear free template~~
11. **Add others modules**
12. ~~SEO optimizations for Google & Yandex~~
13. Add social publisher (Facebook, Twitter, Vkontakte)
14. **Add multi languages support**

# CREATE PROJECT
```
git clone --recursive https://github.com/EndyKaufman/django-postgres-angularjs-blog.git blog
cd blog 
cp _env .env
```

## python env
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib -y
sudo apt-get install python-pip python-dev build-essential -y
sudo apt-get install libpq-dev -y
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
sudo virtualenv venv
source venv/bin/activate
export $(cat .env)
pip install django-toolbelt
pip install -r requirements.txt
```

## frontend tools
```
cd front
sudo npm install -g npm
sudo npm install -g gulpjs/gulp-cli#4.0 karma-cli npm-check-updates bower protractor selenium-webdriver node-gyp git+https://git@github.com/Medium/phantomjs.git#v1.9.19
sudo npm install --save-dev
sudo npm install node-sass --save-dev
sudo npm install gulpjs/gulp#4.0 --save-dev
sudo npm rebuild
gulp webdriver_update
sudo bower install --save --allow-root
```

## run local server
```
source venv/bin/activate
export $(cat .env)
python manage.py collectstatic --noinput
gunicorn project.wsgi -b 0.0.0.0:5000 --workers 3
```

open on browser url http://127.0.0.1:5000 in local pc

#TEST (on Protractor + Selenium with PhantomJS)

## run tests (before run tests, you must run server)
```
export $(cat .env)
cd front
gulp test
```

use custom host

```
export $(cat .env)
cd front
gulp test --host http://127.0.0.1:5000
```

for test one file

```
export $(cat .env)
cd front
gulp test --file tests/account/recovery_access.email.api.js
```

if error in test, you may run tests on debug mode

```
export $(cat .env)
cd front
gulp test --debug true
```

# DEVELOP

## collect static files
```
python manage.py collectstatic --noinput
```

## add new module
```
mkdir app/newmodule
django-admin.py startapp newmodule app/newmodule
cp app/project/__init__.py app/newmodule/__init__.py
cp app/project/actions.py app/newmodule/actions.py
```

modifi __init__.py and actions.py with you work code

add module in project/settings.py on INSTALLED_APPS section

## build frontend on development mode

default on run command "gulp build"

```
cd front
gulp build --env development
```
## build frontend on production mode

```
cd front
gulp build --env production
```

use custom output for static

```
cd front
gulp build --env production --static_dir ../wwwroot
```

# RUN ON WINDOWS WITH VAGRANT

## prepare
```
download and install virtualbox from https://www.virtualbox.org/wiki/Downloads
download and install vagrant from https://www.vagrantup.com/downloads.html
read docs http://www.sitepoint.com/getting-started-vagrant-windows/
```

## clone and prepare project
```
git clone --recursive https://github.com/EndyKaufman/django-postgres-angularjs-blog.git blog
cd blog
vagrant up --provider virtualbox
```
## prepare
```
cd blog
vagrant ssh
cd ../../vagrant
source venv/bin/activate
export $(cat .env)
sudo rm -f db.sqlite3
python manage.py migrate
cd front
gulp build --env development
cd ../
python manage.py collectstatic --noinput
```

## start server
```
cd blog
vagrant ssh
cd ../../vagrant
source venv/bin/activate
export $(cat .env)
gunicorn project.wsgi -b 0.0.0.0:5000 --workers 3
```

## run tests on vagrant
```
cd blog
vagrant ssh
cd ../../vagrant
source venv/bin/activate
export $(cat .env)
cd front
export DISPLAY=:10
gulp test --host http://127.0.0.1:5000 --isvagrant true --display 10
```

## fast prepare + run server and tests
```
cd blog
vagrant ssh
cd ../../vagrant
cp _env .env
cd front
gulp scripts:build && gulp scripts:test
```

## fast run server
```
cd blog
vagrant ssh
cd ../../vagrant
cp _env .env
cd front
gulp scripts:server
```

# NOTES

## for update nodejs and npm
```
cd front
sudo npm install -g npm
sudo curl https://www.npmjs.com/install.sh | sh
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## for update node deps
```
cd front
sudo npm update -g
sudo ncu -u
sudo npm install --save-dev
sudo npm rebuild
sudo ncu -u -m bower
sudo bower install --save --allow-root
```

## if gulp version < 4.0, please update
```
cd front
sudo npm uninstall gulp -g
sudo npm uninstall gulp
sudo npm install gulpjs/gulp-cli#4.0 -g
sudo npm install gulpjs/gulp.git#4.0 --save-dev
```


## commands for reinstall phantom js
```
cd front
sudo rm -r /usr/local/bin/phantomjs
sudo rm -r /usr/lib/node_modules/phantomjs
sudo rm -r /usr/lib/node_modules/.phantomjs.DELETE
sudo npm -g install git+https://git@github.com/Medium/phantomjs.git#v1.9.19
sudo ln -s /usr/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs /usr/local/bin/phantomjs
sudo rm -r node_modules/phantomjs
sudo rm -r node_modules/.phantomjs.DELETE
sudo npm install git+https://git@github.com/Medium/phantomjs.git#v1.9.19 --save-dev
```

## vagrant commands
```
vagrant up
vagrant reload
vagrant resume
```

## django database commands
```
source venv/bin/activate
export $(cat .env)
python manage.py migrate
python manage.py makemigrations
python manage.py makemigrations --empty yourappname
```

## work with git and submodules
```
git submodule add https://github.com/EndyKaufman/django-postgres-angularjs-blog-front.git front
eval "$(ssh-agent -s)"
ssh-add
git config status.submodulesummary 1
git status
git commit -m "updated my submodule"
git submodule update --remote --merge
git push --recurse-submodules=on-demand
git remote remove origin
git remote add origin https://github.com/EndyKaufman/django-postgres-angularjs-blog.git
```

## work with heroku
```
heroku login
heroku ps:scale web=1 --app django-postgres-angularjs-blog
heroku addons:create heroku-postgresql --app django-postgres-angularjs-blog
heroku run python manage.py migrate --app django-postgres-angularjs-blog
heroku run python manage.py createsuperuser --app django-postgres-angularjs-blog
```

## sample work with oauth2 server
```
curl -X POST -d "grant_type=password&username=user&password=user@email.com&client_id=mFyx5LYIpFgeH6e8NkZgNGBkpHRVCiVEBqQJ3yk6&client_secret=tDzxylGEuiOTf7ht6dVjr3MZhR9gZqSFWSVIvKxBzGcUizpZhuwE9AN30VMWojrwvrI5HILMPVKxpdLzOJEhVanVzFoKfo7XfoP0A1SCbiTXOX718KWrdvTk1sr9PcFg" http://127.0.0.1:5000/oauth2/token/
curl 'http://localhost:5000/api/v1/project/update/project1' -H "Authorization: Bearer fLzfISwHUzmpU0I1JyZ6ocfM8ht7G1" --data-binary '{"title":"Changed from api"}'
```

##frontend translated with https://angular-gettext.rocketeer.be
sudo apt-get install poedit
