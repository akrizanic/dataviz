import datetime

from .models import Temps

def parse_csv(datalines):
    tempdata = []
    for l in datalines:
        tempdata.append(l.split(","))
    return tempdata


def fill_db(tempdata):
    for temp in tempdata:
        tdate = datetime.datetime.strptime(temp[0], "%m/%d/%y")
        t = Temps(date = tdate, temp1 = temp[1], temp2 = temp[2], temp3 = temp[3], temp4 = temp[4])
        t.save()

def clean_db():
    Temps.objects.all().delete()
