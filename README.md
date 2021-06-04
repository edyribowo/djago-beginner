# Vaccine Kit Model

## Documentation

1. Download the dataset from https://data.mendeley.com/datasets/hsv83m5zbb/2
2. Divide the data generated in the form of images into two parts : Training Part and Testing Part
3. Preprocessing image using from tensorflow.keras.preprocessing.image
4. Create Pre-trained Deep Learning Model called VGG16 to recognize the faces.
5. Create the training and validation batch using train generator
6. Create image augmentation using ImageDataGenerator
7. Training the model
8. Validating the model
9. Save the model in the .h5 format


# Vaccine Kit API

## Setup

The first thing to do is to clone the repository:

```bash
git clone https://github.com/edyribowo/djago-beginner.git
cd djago-beginner/src
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
