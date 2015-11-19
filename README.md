# chatmessage
 

$ pip install virtualenv

$mkdir vir_env && cd  vir_env 

$virtualenv chat

$git clone https://github.com/SharmaVinayKumar/chatmessage.git

$cd chatmessage

$ pip install -r requirements.txt

$python manage.py syncdb

create super user

$python manage.py migrate

#Run application

$python manage.py runserver

#step to use application

Signup->login->select user->send message



