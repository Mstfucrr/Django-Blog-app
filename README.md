# Django-Blog-app
 
 Başlangıç (cmd)
 
1- pip install Django==version_numarası    version_numarası girilmemiş ise son version indirilir

2- django-admin --version   == > version öğrenmek
3- django-admin startproject proje_ismi     bulunduğu dizinie proje_ismi isminde projeyi oluşturur eg.(blog)
blog içinde (blog/( __init__.py & settings.py & urls.py & wsgi.py) ) & manage.py dosyaları oluşacak
4- Terminal ->  python manage.py runserver ile sunucu (host) port ile açılır ve db oluşur
5- Terminal ->  python manage.py migrate   ile tablolar database'e oluşu (her uygulama sonrasında yapılmalı)
6- Terminal ->  python manage.py createsuperuser ile admin panaline erişen register codu
7- Terminal ->  python manage.py startapp article       article isimli bir uygulama oluşturur
8- 
