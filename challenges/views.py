from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
monthly_challenges = {
    "january": "Red",
    "fabruary":"Blue",
    "march":"green",
    "april":"pink",
    "may":"orange",
    "june":"purple",
    "july":"black",
    "august":"white",
    "september":"burgendy",
    "october":"yellow",
    "november":"darkgreen",
    "december":None
}
# Create your views here.

def index(request):
    
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })

def monthly_challenges_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("enterd number is invalid!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "dates" : month,
           # "NOM" : monthly_challenge.keys(),
            "text" : challenge_text

        })
       
    except:

        raise Http404()
       # response_data = render_to_string("404.html")
       # return HttpResponseNotFound(response_data)
   

    
