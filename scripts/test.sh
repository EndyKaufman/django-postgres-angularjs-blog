#!/bin/bash

source venv/bin/activate
export DISPLAY=:10
cd front
# gulp test --host http://127.0.0.1:5000 --isvagrant true --display 10 --file tests/project/admin.api.js
gulp test --host http://127.0.0.1:5000 --isvagrant true --display 10
cd ../