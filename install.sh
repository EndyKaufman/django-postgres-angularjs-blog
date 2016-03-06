apt-get update
apt-get install -y g++
apt-get autoremove nodejs -y
curl -sL https://deb.nodesource.com/setup_5.x | -E bash -
apt-get install -y nodejs
apt-get install npm -y
npm install -g npm
apt-get install -y git
apt-get install -y default-jre
apt-get install -y default-jdk
apt-get install -y openjdk-7-jre
apt-get install -y openjdk-7-jdk
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
apt-get install xvfb -y
apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps -y
ln -s /usr/bin/nodejs /usr/bin/node
apt-get update
apt-get install google-chrome-stable -y
apt-get install postgresql postgresql-contrib -y
apt-get install python-pip python-dev build-essential -y
apt-get install libpq-dev -y
pip install --upgrade pip
pip install --upgrade virtualenv
npm install -g git+https://git@github.com/gulpjs/gulp.git#4.0
npm install -g karma-cli
npm install -g npm-check-updates
npm install -g bower
npm install -g protractor
npm install -g selenium-webdriver
npm install -g node-gyp
npm rebuild
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd front
npm install --save-dev
npm rebuild
bower install --save --force-latest --allow-root
gulp webdriver_update
cd ../
