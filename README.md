# Modern University
University of Tehran; AP final project :trollface:


# Setup and Run!

first clone the project and enter to the project directory
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


to run the project you should set your own config! 

now we only have a Database config!

to make thet you should insert `DATABASE=your_database_name.sqlite3` in a `.env` file, wich was handeled by `python-dotenv`

to do that just run the command bellow on your terminal
```bash
echo ‘DATABASE=database.sqlite3’ > .env
```

now it's time to create an admin user on the database by run the command bellow and make your own admin user!
```bash
python main.py createadmin
```

everything's done, lets run the project :)
```bash
python main.py
```


# Keep in Touch
check my [website](https://yazdanra.github.io) out, and of course you can contact me on [Telegram](https://t.me/yazdan_ra).


# Documents
you can see the [document](https://github.com/YazdanRa/modern-university/blob/master/docs/ModernUniversity.pdf) on docs directory.
