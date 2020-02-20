from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import Logs
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LogsSerializer
from datetime import datetime

class LogsView(APIView):
    def get(self, request):
        logs = Logs.objects.all()

        serializer = LogsSerializer(logs, many=True)
        return Response({"data": serializer.data})

    def delete(self, request):
        Logs.objects.all().delete()
        return Response({"data": "Done"})

def activateTrackers(requests, id):
    t = Logs.objects.get(id=id)
    
    if len(t) == 0:
        Logs.objects.filter(id = id).update(time = datetime.now())
    else:
        log_entry = Logs(id = id, time = datetime.now())
        log_entry.save()
        
    return HttpResponse("Done")
