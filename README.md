# Vaccine Kit API

## Setup

The first thing to do is to clone the repository:

```bash
git clone https://github.com/edyribowo/djago-beginner.git
cd djago-beginner
```
Create a virtual environment to install dependencies in and activate it:
```bash
pip install virtualenv
virtualenv env
source env/bin/activate
```
Then install the dependencies:

```bash
(env)$ pip install -r requirements.txt
```
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:
```bash
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

In order to test the purchase flows, fill in the account details in ```src/core/views.py``` to match your developer credentials.
