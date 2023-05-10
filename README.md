# CeneoWebScraper

#
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ python -m venv .venv

s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ source .venv/Scripts/activate
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ pip install -r requirements.txt
Collecting beautifulsoup4==4.12.0
  Downloading beautifulsoup4-4.12.0-py3-none-any.whl (132 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 132.2/132.2 kB 2.6 MB/s eta 0:00:00Collecting certifi==2022.12.7
  Downloading certifi-2022.12.7-py3-none-any.whl (155 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.3/155.3 kB 9.1 MB/s eta 0:00:00Collecting charset-normalizer==3.1.0
  Downloading charset_normalizer-3.1.0-cp310-cp310-win_amd64.whl (97 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.1/97.1 kB 5.8 MB/s eta 0:00:00 
Collecting contourpy==1.0.7
  Downloading contourpy-1.0.7-cp310-cp310-win_amd64.whl (162 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 163.0/163.0 kB ? eta 0:00:00      
Collecting cycler==0.11.0
  Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting fonttools==4.39.3
  Downloading fonttools-4.39.3-py3-none-any.whl (1.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 8.0 MB/s eta 0:00:00   
Collecting idna==3.4
  Downloading idna-3.4-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB ? eta 0:00:00        
Collecting kiwisolver==1.4.4
  Downloading kiwisolver-1.4.4-cp310-cp310-win_amd64.whl (55 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.3/55.3 kB ? eta 0:00:00        
Collecting matplotlib==3.7.1
  Downloading matplotlib-3.7.1-cp310-cp310-win_amd64.whl (7.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.6/7.6 MB 9.8 MB/s eta 0:00:00   
Collecting numpy==1.24.3
  Downloading numpy-1.24.3-cp310-cp310-win_amd64.whl (14.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.8/14.8 MB 8.4 MB/s eta 0:00:00 
Collecting packaging==23.1
  Downloading packaging-23.1-py3-none-any.whl (48 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.9/48.9 kB ? eta 0:00:00        
Collecting pandas==2.0.1
  Downloading pandas-2.0.1-cp310-cp310-win_amd64.whl (10.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.7/10.7 MB 7.4 MB/s eta 0:00:00 
Collecting Pillow==9.5.0
  Downloading Pillow-9.5.0-cp310-cp310-win_amd64.whl (2.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 3.9 MB/s eta 0:00:00   
Collecting pyparsing==3.0.9
  Downloading pyparsing-3.0.9-py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.3/98.3 kB 5.9 MB/s eta 0:00:00 
Collecting python-dateutil==2.8.2
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 kB 3.8 MB/s eta 0:00:00Collecting pytz==2023.3
  Downloading pytz-2023.3-py2.py3-none-any.whl (502 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 502.3/502.3 kB 3.5 MB/s eta 0:00:00Collecting requests==2.28.2
  Downloading requests-2.28.2-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 kB 1.7 MB/s eta 0:00:00 
Collecting six==1.16.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting soupsieve==2.4
  Downloading soupsieve-2.4-py3-none-any.whl (37 kB)
Collecting tzdata==2023.3
  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 341.8/341.8 kB 2.1 MB/s eta 0:00:00Collecting urllib3==1.26.15
  Downloading urllib3-1.26.15-py2.py3-none-any.whl (140 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 140.9/140.9 kB 2.1 MB/s eta 0:00:00Installing collected packages: pytz, urllib3, tzdata, soupsieve, six, pyparsing, Pillow, packaging, numpy, kiwisolver, idna, fonttools, cycler, charset-normalizer, certifi, requests, python-dateutil, contourpy, beautifulsoup4, pandas, matplotlib
Successfully installed Pillow-9.5.0 beautifulsoup4-4.12.0 certifi-2022.12.7 charset-normalizer-3.1.0 contourpy-1.0.7 cycler-0.11.0 fonttools-4.39.3 idna-3.4 kiwisolver-1.4.4 matplotlib-3.7.1 numpy-1.24.3 packaging-23.1 pandas-2.0.1 pyparsing-3.0.9 python-dateutil-2.8.2 pytz-2023.3 requests-2.28.2 six-1.16.0 soupsieve-2.4 tzdata-2023.3 urllib3-1.26.15

[notice] A new release of pip available: 22.2.2 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ pip install flask
Collecting flask
  Downloading Flask-2.3.2-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.9/96.9 kB 2.8 MB/s eta 0:00:00 
Collecting Werkzeug>=2.3.3
  Downloading Werkzeug-2.3.4-py3-none-any.whl (242 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.5/242.5 kB 4.9 MB/s eta 0:00:00Collecting Jinja2>=3.1.2
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB ? eta 0:00:00      
Collecting itsdangerous>=2.1.2
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting blinker>=1.6.2
  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)
Collecting click>=8.1.3
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB ? eta 0:00:00        
Collecting colorama
  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.2-cp310-cp310-win_amd64.whl (16 kB)
Installing collected packages: MarkupSafe, itsdangerous, colorama, blinker, Werkzeug, Jinja2, click, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.2 Werkzeug-2.3.4 blinker-1.6.2 click-8.1.3 colorama-0.4.6 flask-2.3.2 itsdangerous-2.1.2

[notice] A new release of pip available: 22.2.2 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ python.exe -m pip install --upgrade pip~
ERROR: Invalid requirement: 'pip~'

[notice] A new release of pip available: 22.2.2 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in d:\227404\ceneowebscraper\.venv\lib\site-packages (22.2.2)
Collecting pip
  Downloading pip-23.1.2-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 6.6 MB/s eta 0:00:00   
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.2.2
    Uninstalling pip-22.2.2:
      Successfully uninstalled pip-22.2.2
Successfully installed pip-23.1.2
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ pip freeze > re
README.md         requirements.txt  
(.venv)
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ pip freeze > requirements.txt
(.venv)
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ git config user.name AndreiHlushchanka
(.venv)
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ git config user.email 227404@student.uek.krakow.pl
(.venv)
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: While importing 'app', an ImportError was raised:

Traceback (most recent call last):
  File "D:\227404\CeneoWebScraper\.venv\lib\site-packages\flask\cli.py", line 218, in locate_app
    __import__(module_name)
  File "D:\227404\CeneoWebScraper\app\__init__.py", line 5, in <module>
    from app import routes
ImportError: cannot import name 'routes' from partially initialized module 'app' (most likely due to a circular import) (D:\227404\CeneoWebScraper\app\__init__.py)

(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ flask run
 * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [10/May/2023 14:34:47] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/May/2023 14:34:48] "GET /favicon.ico HTTP/1.1" 404 -
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ flask run
 * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [10/May/2023 14:39:21] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/May/2023 14:39:23] "GET / HTTP/1.1" 200 -
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$
(.venv) 
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$
(.venv)
s-121-28@K-121-28 MINGW64 /d/227404/CeneoWebScraper (main)
$ flask run
 * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [10/May/2023 14:39:57] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/May/2023 14:39:58] "GET / HTTP/1.1" 200 -













