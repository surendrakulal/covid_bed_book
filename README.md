Instruction To Run The project

Installation
1.install virtualenv globally installed in your computer.
pip install virtualenv

2.Git clone this repo to your PC
git clone https://github.com/surendrakulal/covid_bed_book.git

3.Cd into your the cloned repo.
cd covid_bed_book

4.Create your virtual environment:
virtualenv env

5.Make those migrations work
a.python manage.py makemigrations
b.python manage.py migrate

6.Run server using this one simple command:
python manage.py runserver

7.create superuser
a.python manage.py createsuperuser
a.Username (leave blank to use 'admin'): admin
b.Email address: Admin@gmail.com
c.Password:Admin@123
d.Password (again):Admin@123
