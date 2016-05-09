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
12. SEO optimizations for Google & Yandex
13. Add social publisher (Facebook, Twitter, Vkontakte)
14. Add multi languages support

# RUN ON WINDOWS WITH VAGRANT

## 1. Prepare
```
download and install virtualbox from https://www.virtualbox.org/wiki/Downloads
download and install vagrant from https://www.vagrantup.com/downloads.html
```

## 2. Clone project
```
git clone --recursive https://github.com/EndyKaufman/django-postgres-angularjs-blog.git blog
cd blog
vagrant up --provider virtualbox
```

## 3. Run server
```
cd blog
vagrant ssh
cd ../../vagrant
cp _env .env
cd front
gulp scripts:server
```

## 4. Open browser and navigate to http://127.0.0.1:5000
