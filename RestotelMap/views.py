from django.shortcuts import render
from django.template import RequestContext
from django.template.context import Context
from django.http import JsonResponse
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(
        request,
        'app/index.html',
        {
            'title':'Websig',
        }
    )
    

#def search_view(request):
#    query = request.GET.get('q', '')
#    results = Etab.objects.filter(
#        Q(nom__icontains=query) |
#        Q(local__ville__icontains=query) |
#        Q(local__commune__icontains=query) |
#        Q(local__quartier__icontains=query)
#    )
#
#    # Convertir les coordonnées de la forme (7,04954 -3,9794224) en (7.04954, -3.9794224)
#    for result in results:
#        result.latitude = str(result.latitude).replace(',', '.')
#        result.longitude = str(result.longitude).replace(',', '.')
#
#    context = {'results': results, 'query': query}
#    return render(request, 'app/index.html', context)


def search_view(request):
    query = request.GET.get('q', '')
    
    # Utilisez .first() pour obtenir le premier résultat trouvé
    result = Etab.objects.filter(
        Q(nom__icontains=query) |
        Q(local__ville__icontains=query) |
        Q(local__commune__icontains=query) |
        Q(local__quartier__icontains=query)
    ).first()

    # Convertir les coordonnées de la forme (7,04954 -3,9794224) en (7.04954, -3.9794224)
    if result:
        result.latitude = str(result.latitude).replace(',', '.')
        result.longitude = str(result.longitude).replace(',', '.')

    context = {'result': result, 'query': query}
    return render(request, 'app/index.html', context)

