# django-postgres-angularjs-blog
  Simple blog written on django + angularjs and use postgre sql as database

https://django-postgres-angularjs-blog.herokuapp.com


## current progress of project

in process

# CREATE PROJECT
```
git clone https://github.com/EndyKaufman/django-postgres-angularjs-blog.git blog 
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
sudo npm install -g gulpjs/gulp-cli#4.0 gulpjs/gulp#4.0 karma-cli npm-check-updates bower protractor selenium-webdriver git+https://git@github.com/Medium/phantomjs.git##v1.9.19 node-sass
sudo npm install --save-dev
sudo bower install --save --allow-root
gulp webdriver_update
```

## run local server
```
source venv/bin/activate
export $(cat .env)
python manage.py livereload
```

open url http://127.0.0.1:5000

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

## build frontend file (gulp dev / gulp public)
```
cd front
gulp dev
```

#TEST (on Protractor + Selenium with PhantomJS)

## run tests (before run tests, you must run local server on http://127.0.0.1:5000)
```
cd front
gulp test
```

# RUN ON WINDOWS WITH VAGRANT

## prepare
```
download and install virtualbox from https://www.virtualbox.org/wiki/Downloads
download and install vagrant from https://www.vagrantup.com/downloads.html
read docs http://www.sitepoint.com/getting-started-vagrant-windows/
```

## clone project and run from this folder vagrant init & vagrant up
```
git clone https://github.com/EndyKaufman/django-postgres-angularjs-blog.git blog 
cd blog
vagrant up
vagrant ssh
cd ../../vagrant
python.py manage livereload
```

## run tests on vagrant
```
cd blog
vagrant ssh
cd ../../vagrant/front
gulp test
```

## build front on vagrant
```
cd blog
vagrant ssh
cd ../../vagrant/front
gulp dev
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

