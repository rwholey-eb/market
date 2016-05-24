echo 'CREATE DATABASE IF NOT EXISTS market_db' | mysql -u root

virtualenv -p /usr/bin/python venv
. ./venv/bin/activate
pip install -r ./requirements.txt