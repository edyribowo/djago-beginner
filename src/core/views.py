import simplejson as simplejson
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

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

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_vaccine_data(request):
    result = db.collection('users').where('nik', "==", "12731873618736918").stream()
    for doc in result:
        data = simplejson.dumps(doc.to_dict())
        return HttpResponse(data, content_type='application/json')

class TestView(APIView):
    # def get(self, request, *args, **kwargs):
    #     qs = Post.objects.all()
    #     post = qs.first()
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        result = db.collection('users').where('nik', "==", "12731873618736918").stream()
        for doc in result:
            return Response(doc.to_dict())

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            db.collection('users').add(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors)
