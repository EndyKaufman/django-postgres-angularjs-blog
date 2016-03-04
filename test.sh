source venv/bin/activate
export $(cat .env)
export DISPLAY=:10
cd front
gulp test --host http://127.0.0.1:5000 --isvagrant true --file_ project/admin.js --debug true --display 10
cd ../