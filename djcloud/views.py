from django.shortcuts import render
import pyrebase
# Create your views here.
config={
    "apiKey": "AIzaSyCvSlipnTy4kwvMz7DfUdDo4RPc5h6TiNM",
    "authDomain": "cloud-89b5d.firebaseapp.com",
    "databaseURL": "https://cloud-89b5d-default-rtdb.firebaseio.com",
    "projectId": "cloud-89b5d",
    "storageBucket": "cloud-89b5d.appspot.com",
    "messagingSenderId": "553760390891",
    "appId": "1:553760390891:web:acf917d0f79f610c8d88ae",
}

firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()

def index(request):
    encrpytdata=database.child('Data').child('name').get().val()
    #decrpytdata=database.child('Data').child('dedata').get().val()
    return render(request,'index.html',{
        "edt":encrpytdata
    })