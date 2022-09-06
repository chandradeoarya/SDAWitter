## SDA + Twitter = SDAWitter

<h3 align="center">
SDAWitter (Twitter for SDA bootcamp students)
</h3>

This is a simple but fully functional Twitter clone built in Django framework using Docker and kubernetes and deployed in EKS with persistent volume. The project aims to show a simple yet standard way of developing and deploying django applications on docker and kubernetes. 

<p align="center">
  <img src = "https://github.com/chandradeoarya/SDAWitter/blob/master/SDAWitter.gif?raw=true" width=600>
</p>

### Contributors

#### Developers
- Nathan Bell
- Chandradeo Arya

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
# go back to the project folder 
cd .. 
cd ..
pip3 install -r requirements.txt

#Run code
python manage.py runserver

```

##### Notes
- For easiness database is committed but use postgres in production with migrations.
