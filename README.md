## SDA + Twitter = SDAWitter

## Requirements
- Python3 installed
- Pip3 installed
#### How to run the code

```sh
#Create virtual env
python3 -m venv venv

#Activate venv
source venv/bin/activate

#Install libraries
pip3 install -r requirements.txt

#Run code
python3 manage.py runserver

```
#### How to run the code in windows 
#### Note : run all commands inside the project folder 

```sh
# install virtual env:
pip install virtualenv

#Create virtual env:
virtualenv env

#Activate your virtual env:
cd env/Scripts
.\activate

#Install libraries
pip3 install -r requirements.txt

#Run code
python manage.py runserver

```

##### Notes
- For easiness database is committed but use postgres in production with migrations.
