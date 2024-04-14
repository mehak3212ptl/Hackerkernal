from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import  HttpResponse,JsonResponse
from .models import *
from app.serializers import UsersSerializer
import pandas as pd
import uuid 
# import os 
from rest_framework.response import Response

# Create your views here.

def createexcel(request):   
    all_data=User.objects.all()
    serializer=UsersSerializer(all_data,many=True)
    df = pd.DataFrame(serializer.data)
    print(df)
    df.to_csv(f"media/{uuid.uuid4}.xls",encoding="UTF-8",index=False)
    return HttpResponse({"status":200},content_type="applications/json")

