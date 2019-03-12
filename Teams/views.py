from django.shortcuts import render

# Create your views here.
def Teams(response):
    return render(response,'Teams/teams.html')