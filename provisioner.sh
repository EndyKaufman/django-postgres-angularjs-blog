apt-get update
sudo apt-get install -y g++
sudo apt-get autoremove nodejs -y
curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install -y git
sudo apt-get install -y default-jre
sudo apt-get install -y default-jdk
sudo apt-get install -y openjdk-7-jre
sudo apt-get install -y openjdk-7-jdk
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib -y
sudo apt-get install python-pip python-dev build-essential -y
sudo apt-get install libpq-dev -y
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
sudo apt-get install npm -y
sudo npm install -g npm
sudo npm install -g gulpjs/gulp-cli#4.0
sudo npm install -g karma-cli
sudo npm install -g npm-check-updates
sudo npm install -g bower protractor
sudo npm install -g protractor
sudo npm install -g selenium-webdriver
sudo npm install -g node-gyp
sudo npm install -g git+https://git@github.com/Medium/phantomjs.git#v1.9.19
cd ../../vagrant
cp _env .env
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd front
sudo npm install gulpjs/gulp#4.0 --save-dev
sudo npm install --save-dev
sudo npm install node-sass --save-dev
sudo npm rebuild
gulp webdriver_update
sudo bower install --save --allow-root
