# modern-university
University of Tehran; AP final project


# setup and run
```shell
git clone https://github.com/YazdanRa/modern-university.git
cd modern-university
sudo apt-get install virtualenv
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
‘DATABASE=database.sqlite3’ > .env
python main.py
```
