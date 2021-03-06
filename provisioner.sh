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
sudo apt-get install firefox -y
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get install xvfb -y
sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps -y
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo apt-get update
sudo apt-get install google-chrome-stable -y
sudo apt-get install postgresql postgresql-contrib -y
sudo apt-get install python-pip python-dev build-essential -y
sudo apt-get install libpq-dev -y
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
sudo apt-get install npm -y
sudo npm install -g npm
sudo npm install -g git+https://git@github.com/gulpjs/gulp.git#4.0
sudo npm install -g karma-cli
sudo npm install -g npm-check-updates
sudo npm install -g bower
sudo npm install -g protractor
sudo npm install -g selenium-webdriver
sudo npm install -g node-gyp
sudo npm install -g git+https://git@github.com/Medium/phantomjs.git#v1.9.19
cd ../../vagrant
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd front
sudo npm install node-sass --save-dev --no-bin-links
sudo npm install --save-dev --no-bin-links
sudo npm install git+https://git@github.com/gulpjs/gulp.git#4.0 --save-dev --no-bin-links
sudo npm rebuild
sudo rm -rf node_modules/.staging
sudo npm install --save-dev --no-bin-links
sudo npm rebuild
sudo bower install --save --force-latest --allow-root
gulp webdriver_update
