from django.shortcuts import render
from .models import Case, VerifiedLead, BlogArticle
import datetime

import requests
username = "covidhelpadgitm"
api_token = "20f4d866b7249ebf458572028d4d2b3f9ac24dc6"
domain_name = "covidhelp.pythonanywhere.com"

def AddPlusKey(param):
    return param if '-' in param else '+' + param

try:
    currentCase = Case.objects.all()[len(Case.objects.all()) - 1]

    total = currentCase.total
    death = currentCase.death
    recovered = currentCase.recovered
    active = currentCase.active
    date = currentCase.date.__str__()
    date = date.replace( date[date.index(':')+3:len(date)], '')

except:
    total = 'data unavailable'
    death = 'data unavailable'
    recovered = 'data unavailable'
    active = 'data unavailable'
    date = 'data unavailable'

    newTotal = 'data unavailable'
    newDeath = 'data unavailable'
    newActive = 'data unavailable'
    newRecovered = 'data unavailable'
    newDate = 'data unavailable'

else:
    try:
        lastCase  = Case.objects.all()[len(Case.objects.all()) - 2]

        newTotal = AddPlusKey(str(int(total) - int(lastCase.total)))
        newDeath = AddPlusKey(str(int(death) - int(lastCase.death)))
        newRecovered = AddPlusKey(str(int(recovered) - int(lastCase.recovered)))
        newActive = AddPlusKey(str(int(active) - int(lastCase.active)))
        newDate = (currentCase.date - lastCase.date).__str__()
        newDate = newDate[0:newDate.index(':')] + ' hours'

    except:
        newTotal = '+0'
        newDeath = '+0'
        newActive = '+0'
        newRecovered = '+0'
        newDate = ''

try:
    VerifiedLeads = VerifiedLead.objects.all()
except:
    VerifiedLeads = []

def HomePage(request):
    if request.method == 'GET' and 'databaseupdatekey' in request.GET:
        if request.GET['databaseupdatekey'] == 'covidhelpadgitmdatabaseupdatekeytrueforcasesupdate':
            Case(total=request.GET['total'], active=request.GET['active'], death=request.GET['death'], recovered=request.GET['recovered']).save()
            response = requests.post(
                'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
                    username=username, domain_name=domain_name
                ),
                headers={'Authorization': 'Token {token}'.format(token=api_token)}
            )
            if response.status_code == 200:
                pass
            else:
                exit()
        elif request.GET['databaseupdatekey'] == 'covidhelpadgitmdatabaseupdatekeytrueforverifiedleadsupdate':
            VerifiedLead(Timestamp=datetime.datetime.strptime(request.GET['timestamp'], '%Y-%m-%d %H:%M:%S'), Supplier=request.GET['supplier'], Resource=request.GET['resource'], Contact=request.GET['contact'], Remarks=request.GET['remarks']).save()
    data = {
        'total':total,
        'death':death,
        'active':active,
        'recovered':recovered,
        'date':date,

        'newTotal':newTotal,
        'newDeath':newDeath,
        'newActive':newActive,
        'newRecovered':newRecovered,
        'newDate':newDate,

        'VerifiedLeads':VerifiedLeads
    }
    return render(request, 'Covid.html', data)

def AboutPage(request):
    return render(request, 'About.html')

def BlogPage(request):
    data = {
        'blog' : BlogArticle.objects.all()
    }
    return render(request, 'Blog.html', data)

def VaccinePage(request):
    return render(request, 'Vaccine.html')

def ArticlePage(request):
    return render(request, 'Single.html')