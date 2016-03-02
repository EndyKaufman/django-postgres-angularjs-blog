source venv/bin/activate
export $(cat .env)
export DISPLAY_=:10
cd front
gulp test --host http://127.0.0.1:5000 --isvagrant_ true --file_ project/admin.js --debug_ true
cd ../