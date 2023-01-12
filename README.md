# Logging app setup instruction (Debian/WSL2)

## Clone code from Git to any folder
```
krisplis@localhost:/some/location$ tree
.
├── app.py
├── requirements.txt
├── README
└── stronka
    ├── __init__.py
    ├── create_db.py
    ├── forms.py
    ├── models.py
    ├── routes.py
    ├── scrapper
    │   ├── __init__.py
    │   ├── chromedriver.exe
    │   ├── scraper_readme.md
    │   └── selenium_scraper.py
    ├── static
    │   ├── css
    │   │   ├── bootstrap.min.css
    │   │   ├── login_register.css
    │   │   ├── style.css
    │   │   └── styles.css
    │   └── img
    │       ├── background.png
    │       └── logo.png
    └── templates
        ├── base.html
        ├── index.html
        ├── login.html
        └── signin.html

6 directories, 22 files
```

## Setup postgres database
```
krisplis@localhost:/some/location$ sudo service postgresql start
 * Starting PostgreSQL 12 database server                                                                                                            [ OK ]
krisplis@localhost:/some/location$ sudo psql -h localhost -p 5432 -U postgres
psql (12.13 (Ubuntu 12.13-0ubuntu0.20.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

postgres=# ALTER USER postgres WITH PASSWORD [password];
ALTER USER
postgres=#\q
```

## Provide postgres username and password (inside []) in __init__.py file
```
9   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://[username]:[password]@localhost:5432'
```

## Make sure postgres is running on localhost:5432
```
krisplis@localhost:/some/location$ service postgresql status
12/main (port 5432): online
krisplis@localhost:/some/location$ netstat -tulpn | grep 5432
(No info could be read for "-p": geteuid()=1000 but you should be root.)
tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      -
krisplis@localhost:/some/location$
```

## Make sure you have Python 3.8.10 (or newer) and pip 20.0.2 (or newer) installed
```
krisplis@LAPTOP-3B7TF2NS:/mnt/c/Users/Krzychu/Desktop/Studia/V semestr/IO_Project_A2$ python3 --version
Python 3.8.10
krisplis@LAPTOP-3B7TF2NS:/mnt/c/Users/Krzychu/Desktop/Studia/V semestr/IO_Project_A2$ pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
krisplis@LAPTOP-3B7TF2NS:/mnt/c/Users/Krzychu/Desktop/Studia/V semestr/IO_Project_A2$
```
If not install python and pip
```
krisplis@localhost:/some/location$ apt-get upgrade
.
.
.
krisplis@localhost:/some/location$ apt install python3
.
.
.
krisplis@localhost:/some/location$ apt install pip
.
.
.
```

## Install all project requirements
```
krisplis@localhost:/some/location$ pip install -r requirements
```

## Initialise database
```
krisplis@localhost:/some/location$ python3 stronka/create_db.py
/usr/local/lib/python3.8/dist-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
```

## Start debug server
```
krisplis@localhost:/some/location$ python3 app.py
/usr/local/lib/python3.8/dist-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
 * Serving Flask app 'stronka'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
You can now enter this address and logging should work now properly

## Known bugs
### If database won't initialise because of this error:
```
krisplis@localhost:/some/location$ python3 stronka/create_db.py
Traceback (most recent call last):
  File "stronka/create_db.py", line 1, in <module>
    from stronka import db
ModuleNotFoundError: No module named 'stronka'
```
This means that your Python environment doesn't know module "stronka" and needs to be told where it is located
### SOLUTION: Modify python path
```
krisplis@localhost:/some/location$ export PYTHONPATH=/some/location/stronka:$PYTHONPATH
```
Now everything should work fine
```
krisplis@localhost:/some/location$ python3 stronka/create_db.py
/usr/local/lib/python3.8/dist-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
```
