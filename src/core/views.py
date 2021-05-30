import simplejson as simplejson
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import tensorflow as tf

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post
from keras.preprocessing import image
import numpy as np

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_vaccine_data(request):
    result = db.collection('users').where('nik', "==", "{}".format(request.query_params.get('nik'))).stream()
    data = []
    for doc in result:
        data = simplejson.dumps(doc.to_dict())
        return HttpResponse(data, content_type='application/json')


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def photo_verification(request):
    result = db.collection('users').where('nik', "==", "{}".format(request.query_params.get('nik'))).stream()
    data = []
    imageName = "{}".format(request.query_params.get('photo'))
    model = tf.keras.models.load_model('CatVsDogs.h5')
    img = image.load_img('src/images/' + str(imageName), target_size=(300, 400))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    result = ''
    if classes[0][0]<0.5:
        result = 'Dog'
    else:
        result = 'Cat'

    data = simplejson.dumps(result)
    return HttpResponse(data, content_type='application/json')


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
