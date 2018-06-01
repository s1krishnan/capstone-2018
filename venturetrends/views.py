from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def venturetrends_home(request):
    return render(request, 'venturetrends/venturetrends_home.html', {})

@login_required
def home(request):
    if request.user.profile.user_type == 'company':
        return render(request, 'venturetrends/home_company.html', {})
    elif request.user.profile.user_type == 'vc':
        return render(request, 'venturetrends/home_vc.html', {})
    elif request.user.profile.user_type == 'admin':
        return render(request, 'venturetrends/home_admin.html', {})

@login_required()
def it1(request):
    return render(request, 'venturetrends/it1.html', {})

@login_required()
def it2(request):
    return render(request, 'venturetrends/it2.html', {})

@login_required()
def comparecompanies(request):
    return render(request, 'venturetrends/comparecompanies.html', {})

@login_required()
def viewmyinvestments(request):
    return render(request, 'venturetrends/viewmyinvestments.html', {})

@login_required()
def investordetails(request):
    return render(request, 'venturetrends/investordetails.html', {})



