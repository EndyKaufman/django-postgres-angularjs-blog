# django-postgres-angularjs-blog
  Simple blog written on django + angularjs and use postgre sql as database

https://django-postgres-angularjs-blog.herokuapp.com


## current progress of project

1. ~~Write function tests work on Protractor + Selenium with PhantomJS~~
2. ~~Move to Vagrant~~
3. ~~Make templates and tests for basic edit mode~~
4. ~~Add test database on sqlite and move it mock data from tests~~
5. ~~Make all methods and classes for authorization~~
6. **Move frontend code to submodule**
7. Migrate production to Postres SQL
8. Add uppload files from admin mode to Amazone S3
9. Make other parts (copy+past)
10. Change standart bootstrap theme to beautiful and clear free template
11. SEO optimizations for Google & Yandex
12. Add social publisher (Facebook, Twitter, Vkontakte)

# CREATE PROJECT
```
git clone --recursive git@github.com:EndyKaufman/django-postgres-angularjs-blog.git blog
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
virtualenv venv
source venv/bin/activate
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
gunicorn project.wsgi -b 0.0.0.0:5000
```

open on browser url http://127.0.0.1:5000 in local pc

#TEST (on Protractor + Selenium with PhantomJS)

## run tests (before run tests, you must run local server)
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
gulp test --file account/recovery_access.email.api.js
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
git clone --recursive git@github.com:EndyKaufman/django-postgres-angularjs-blog.git blog
cd blog
vagrant init ubuntu/trusty64
vagrant up --provider virtualbox
```

## start server
```
cd blog
vagrant ssh
cd ../../vagrant
source venv/bin/activate
source env.sh
gunicorn project.wsgi -b 0.0.0.0:5000
```

## run tests on vagrant
```
cd blog
vagrant ssh
cd ../../vagrant
source env.sh
cd front
gulp test
```

## build front on vagrant
```
cd blog
vagrant ssh
cd ../../vagrant/front
gulp build
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
sudo npm update --save-dev 
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
python manage.py migrate
python manage.py makemigrations
python manage.py makemigrations --empty yourappname
```

## work with submodules
```
eval "$(ssh-agent -s)"
ssh-add
git config status.submodulesummary 1
git status
git commit -m "updated my submodule"
git submodule update --remote --merge
git push --recurse-submodules=on-demand
git remote remove origin
git remote add origin git@github.com:EndyKaufman/django-postgres-angularjs-blog.git
```