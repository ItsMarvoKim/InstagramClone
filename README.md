# Instagram Clone
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Description
This a web application built using Python, Django and Postgresql.The app is basically a clone of the instagram app, you can post photos under your account and view them on your profile page. As a user you follow other users and other users can follow you. As a user you can like pictures and leave a comment on them, as well as interacting with django's authentication system, as well as uploading images, building a profile page in django


## Author

Marvin Kimathi

# Installation

## Clone
    
```bash
    git clone https://github.com/ItsMarvoKim/InstagramClone.git
    
```
##  Create virtual environment
```bash
    python3.8 -m venv --without-pip virtual
    
```
## Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate
   $ pip install - requirements.txt
    
```
## Run initial migration
```bash
   $ python3.8 manage.py makemigrations instagram
   $ python3.8 manage.py migrate
    
```


## Run app
```bash
   $ python3 manage.py runserver
    
```

## Test class

```bash
    $ python3 manage.py test
```
## Known Bugs


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used

    Python Shell
    Python 3.8
    Django
    Bootstrap
    HTML
    CSS
    PostgreSQL

## License

[LICENSE](LICENSE)




