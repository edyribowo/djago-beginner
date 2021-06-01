import random
import string
import time

import simplejson as simplejson
from django.http import JsonResponse, HttpResponse
import tensorflow as tf

import firebase_admin
import pyrebase
import simplejson
from firebase_admin import credentials
from firebase_admin import firestore
import os
import re

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .serializers import PostSerializer
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
firebase = pyrebase.initialize_app(config)
firebase_storage = firebase.storage()


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_vaccine_data(request):
    """
    description: This API deletes/uninstalls a device.
    parameters:
      - name: name
        type: string
        required: true
        location: form
      - name: bloodgroup
        type: string
        required: true
        location: form
      - name: birthmark
        type: string
        required: true
        location: form
    """
    result = db.collection('users').where('nik', "==", "{}".format(request.query_params.get('nik'))).stream()
    data = []
    for doc in result:
        data = simplejson.dumps(doc.to_dict())
        return HttpResponse(data, content_type='application/json')


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_vaccine_data_email(request):
    result = db.collection('users').where('email', "==", "{}".format(request.query_params.get('email'))).stream()
    data = []
    for doc in result:
        data = simplejson.dumps(doc.to_dict())
        return HttpResponse(data, content_type='application/json')


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_vaccine_data_barcode(request):
    result = db.collection('users').where('barcode', "==", "{}".format(request.query_params.get('barcode'))).stream()
    data = []
    for doc in result:
        data = simplejson.dumps(doc.to_dict())
        return HttpResponse(data, content_type='application/json')


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def photo_verification(request):
    nameFile = "{}".format(request.query_params.get('photo'))
    path_local = "/src/images/"
    path_on_cloud = "photo_request_verif/"

    firebase_storage.child(path_on_cloud+nameFile).download(nameFile)
    time.sleep(5)
    result = db.collection('users').where('nik', "==", "{}".format(request.query_params.get('nik'))).stream()

    model = tf.keras.models.load_model('face_detection_no_dropout.h5')

    img = image.load_img(str(nameFile), target_size=(224, 224, 3))
    test1 = image.img_to_array(img)
    timg = np.expand_dims(test1, axis=0)
    y_pred = model.predict(timg)
    resultz = np.argmax(y_pred, axis=1)
    nikHasil = str(resultz[0]+1)

    finalNIK =""
    for x in range(16-len(nikHasil)):
      finalNIK = finalNIK+'0'

    finalNIK = finalNIK+nikHasil

    barcode = "{}".format(request.query_params.get('nik'))+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=20))
    if finalNIK == request.query_params.get('nik'):
        for doc in result:
            key = doc.id
            db.collection('users').document(key).update({"bsrcode": "{}".format(barcode)})
        data = {
            "verification": "ok",
            "barcode": "{}".format(barcode)
        }
    else:
        data = {
            "verification": "false",
        }
    os.remove(nameFile)
    return HttpResponse(simplejson.dumps(data), content_type='application/json')


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def add_data_vaccine(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        db.collection('users').add(serializer.data)
        return HttpResponse(simplejson.dumps(serializer.data), content_type='application/json')
    return HttpResponse(serializer.errors)


@api_view(('PUT',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def update_vaccine_data(request):
    serializer = PostSerializer(data=request.data)
    result = db.collection('users').where('nik', "==", "{}".format(request.query_params.get('nik'))).stream()
    if serializer.is_valid():
        print("DATA : "+str(serializer.data))
    for doc in result:
        key = doc.id
        db.collection('users').document(key).update(serializer.data)
    data = simplejson.dumps(doc.to_dict())
    return HttpResponse(data, content_type='application/json')


@api_view(('DELETE',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def delete_vaccine_data(request):
    serializer = PostSerializer(data=request.data)
    result = db.collection('users').where('nik', "==", "{}".format(request.query_params.get('nik'))).stream()
    for doc in result:
        key = doc.id
        db.collection('users').document(key).delete()
        return HttpResponse(status=200)


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def verification_account_using_nik(request):
    result = db.collection('users').where('nik', "==", "{}".format(request.query_params.get('nik'))).stream()
    y_dict = { el.id: el.to_dict() for el in result }

    if str(y_dict) == "{}":
        return JsonResponse(status=404, data={'status':'false','message':'Data tidak ditemukan'})
    else:
        return JsonResponse(status=200, data={'status':'true','message':'Data ditemukan'})
