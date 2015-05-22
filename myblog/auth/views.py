from django.shortcuts import render
from django.contrib.auth import authenticate
import mongoengine
# Create your views here.

user = authenticate(username='frank', password='foanaghhf')
assert isinstance(user, mongoengine.django.auth.User)	
