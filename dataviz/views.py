from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from dataviz.datautils import parse_csv, fill_db, clean_db
from dataviz.models import Temps

def upload(request):
    if request.method == "GET":
        return render(request, 'dataviz/upload.html')
    elif request.method == "POST":
        csvfile = request.FILES["csvfile"]

        try:
            uf = csvfile.read().decode("utf-8")
            lines = uf.splitlines()
            tempdata = parse_csv(lines)

            clean_db()
            fill_db(tempdata)

        except UnicodeDecodeError as e:
            return HttpResponse("Must be text file.")
        except ValueError as e:
            return HttpResponse("Bad CSV format.")



        return HttpResponseRedirect(reverse('dataviz:plot'))

def data(request):
    temps = serializers.serialize("json", Temps.objects.all())
    return HttpResponse(temps)

def plot(request):
    return render(request, 'dataviz/plot.html')
