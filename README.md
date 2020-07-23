# modern-university
University of Tehran; AP final project


# setup and run

first clone the project and enter to the directory
```bash
git clone https://github.com/YazdanRa/modern-university.git
```
```bash
cd modern-university
```


then install Virtualenv(if you don't have that already)
```bash
sudo apt-get install virtualenv
```


lets make an virtual environment with python3 and active it
```bash
virtualenv -p python3 .venv
```
```bash
source .venv/bin/activate
```


now you should see `(.venv)` at the first of the line lets install requirements by run command bellow
```bash
pip install -r requirements.txt
```


to run the project you should set your own config! now we only have a Database config to make the config you should add `DATABASE=your_database_name.sqlite3` in a `.env` file to do that just run the command bellow on your terminal
```bash
echo ‘DATABASE=database.sqlite3’ > .env
```

now to create a admin user on the database by run the command bellow and make your admin user!
```bash
python main.py createadmin
```

lets run the project :)
```bash
python main.py
```


# Keep in Touch
check my [website](https://yazdanra.github.io) out, and of course you can contact me on [Telegram](https://t.me/yazdan_ra).


# Documents
you can see the [document](https://github.com/YazdanRa/modern-university/blob/master/docs/ModernUniversity.pdf) on docs directory.
