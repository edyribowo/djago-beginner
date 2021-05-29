import firebase_admin
import simplejson
from firebase_admin import credentials
from firebase_admin import firestore
import re

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

result = db.collection('users').where('nik', "==", "12731873618736918").stream()
data = []
for doc in result:
    data = doc.to_dict()
imageName = data.get('photo')
print(imageName)

