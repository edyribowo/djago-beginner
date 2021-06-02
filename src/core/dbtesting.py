import random
import string
import time

import firebase_admin
import pyrebase
import simplejson
from firebase_admin import credentials
from firebase_admin import firestore
import os
import re
import tensorflow as tf
from keras.preprocessing import image
import numpy as np

 cred = credentials.Certificate("serviceAccountKey.json")
 firebase_admin.initialize_app(cred)
 db = firestore.client()
 config = {
     "apiKey": "AIzaSyBCUiLMdRn3Urnec6BfC4f2UI19v3c8Vs4",
     "authDomain": "vaccinekit-ffd28.firebaseapp.com",
     "projectId": "vaccinekit-ffd28",
     "storageBucket": "vaccinekit-ffd28.appspot.com",
     "messagingSenderId": "548541796934",
     "databaseURL":"",
     "appId": "1:548541796934:web:326a0a8850ee565bf77047",
     "measurementId": "G-4XHMZY181K"
 }
 db = firestore.client()
 firebase = pyrebase.initialize_app(config)
 firebase_storage = firebase.storage()

#
# nameFile = "1234567890.jpeg"
# path_local = "../src/images/"
# path_on_cloud = "photo_request_verif/"

# print("iniNik?"+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=20)))

# firebase_storage.child(path_on_cloud+nameFile).download(path_local+nameFile)

# result = db.collection('users').where('nik', "==", "12731873618736918").stream()
# data = []
# for doc in result:
#     data = doc.to_dict()
# imageName = data.get('photo')
# print(imageName)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
config = {
    "apiKey": "AIzaSyBCUiLMdRn3Urnec6BfC4f2UI19v3c8Vs4",
    "authDomain": "vaccinekit-ffd28.firebaseapp.com",
    "projectId": "vaccinekit-ffd28",
    "storageBucket": "vaccinekit-ffd28.appspot.com",
    "messagingSenderId": "548541796934",
    "databaseURL":"",
    "appId": "1:548541796934:web:326a0a8850ee565bf77047",
    "measurementId": "G-4XHMZY181K"
}
firebase = pyrebase.initialize_app(config)
firebase_storage = firebase.storage()

nameFile = "0000000000000001.jpg"
path_local = "/src/images/"
path_on_cloud = "photo_request_verif/"

firebase_storage.child(path_on_cloud+nameFile).download(nameFile)
time.sleep(5)
result = db.collection('users').where('nik', "==", "{}".format(nameFile)).stream()

imageName = nameFile
model = tf.keras.models.load_model('../face_detection_no_dropout.h5')

img = image.load_img(str(imageName), target_size=(224, 224, 3))
test1 = image.img_to_array(img)
timg = np.expand_dims(test1, axis=0)
y_pred = model.predict(timg)
resultz = np.argmax(y_pred, axis=1)
nikHasil = str(resultz[0]+1)

finalNIK =""
for x in range(16-len(nikHasil)):
  finalNIK = finalNIK+'0'

finalNIK = finalNIK+nikHasil
print(finalNIK)
