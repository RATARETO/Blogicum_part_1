# Проект Блогикум
представляет собой сайт написанный на Django, для публикации постов

## Структура проекта
<pre>
  blogicum
│   db.sqlite3
│   manage.py
│   secret.env
│
├───blog
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           __init__.cpython-312.pyc
│   │
│   └───__pycache__
│           admin.cpython-312.pyc
│           apps.cpython-312.pyc
│           models.cpython-312.pyc
│           urls.cpython-312.pyc
│           views.cpython-312.pyc
│           __init__.cpython-312.pyc
│
├───blogicum
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__
│           settings.cpython-312.pyc
│           urls.cpython-312.pyc
│           wsgi.cpython-312.pyc
│           __init__.cpython-312.pyc
│
├───pages
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           __init__.cpython-312.pyc
│   │
│   └───__pycache__
│           admin.cpython-312.pyc
│           apps.cpython-312.pyc
│           models.cpython-312.pyc
│           urls.cpython-312.pyc
│           views.cpython-312.pyc
│           __init__.cpython-312.pyc
│
├───static
│   ├───css
│   │       bootstrap.min.css
│   │
│   └───img
│       │   logo.png
│       │
│       └───fav
│               android-chrome-192x192.png
│               android-chrome-256x256.png
│               apple-touch-icon.png
│               favicon-16x16.png
│               favicon-32x32.png
│               favicon.ico
│               mstile-150x150.png
│
└───templates
    │   base.html
    │
    ├───includes
    │       footer.html
    │       header.html
    │
    └───posts
            about.html
            category.html
            detail.html
            index.html
            rules.html
</pre>

## проекта поделён на 2 приложения
### blog - основа, отвечает за отображения постов
### pages - отвечает за отображение информации о проекте

## Импорты
1. ﻿asgiref==3.11.0
2. attrs==25.4.0
3. colorama==0.4.6
4. Django==3.2.16
5. dotenv==0.9.9
6. flake8==5.0.4
7. flake8-docstrings==1.7.0
8. iniconfig==2.3.0
9. mccabe==0.7.0
10. packaging==25.0
11. pep8-naming==0.13.3
12. pluggy==1.6.0
13. py==1.11.0
14. pycodestyle==2.9.1
15. pydocstyle==6.3.0
16. pyflakes==2.5.0
17. pytest==7.1.3
18. pytest-django==4.5.2
19. pytest-pythonpath==0.7.3
20. python-dotenv==1.2.1
21. pytz==2025.2
22. snowballstemmer==3.0.1
23. sqlparse==0.5.3
24. tomli==2.3.0
    
#### в процессе создания проекта были использованы flake8 и pytest

#### чтобы импортировать из файла все библиотеки сразу воспользуйтесь командой 
<pre>pip install -r requirements.txt</pre>
