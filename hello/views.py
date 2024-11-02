from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Firma
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramWordSimilarity
from unidecode import unidecode
import csv
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Firma



# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

@login_required
def details(request, id):
  firma = Firma.objects.get(pib=id)
  context = {
    'firma': firma,
  }
  return render(request,'details.html',context)


def home2(request):
    return render(request,'home2.html')


@login_required
def search_firme(request):
    searched = request.GET.get('searched', '')
    if searched:
        if searched.isdigit():
            firme = Firma.objects.filter(pib=searched)
        else:
            firme = Firma.objects.annotate(
                similarity=TrigramWordSimilarity(unidecode(searched), "naziv__unaccent")
            ).filter(similarity__gt=0.7).order_by("-similarity")
        
        paginator = Paginator(firme, 20)  # Show 20 results per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'searched': searched,
            'page_obj': page_obj,
        }
        return render(request, 'search_firme.html', context)
    else:
        return render(request, 'search_firme.html', {'searched': searched}) 

@login_required    
def company_index(request):
    company_list = Firma.objects.all()
    paginator = Paginator(company_list, 20)  # Show 20 companies per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'company_index.html', {'page_obj': page_obj})


@login_required 
def about(request):
    return render(request, 'about.html')
     