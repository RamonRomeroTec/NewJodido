from django.shortcuts import render

# Create your views here.
from lugares.models import Ciudad, Estado, Pais, Lugar, Imagen
from django.http import HttpResponse
import  pprint
from django.http import JsonResponse
from itertools import chain


#Visualizar partidos en la landing page
def landing(request):
    if request.method == 'POST':
        fullname = request.POST['city']
        parsedlocation = fullname.split(', ')
        city = parsedlocation[0]
        state = parsedlocation[1]
        country = parsedlocation[2]
        qpais = Pais.objects.get(nombre=country)
        qstate = Estado.objects.filter(pais=qpais).get(nombre=state)
        qcity = Ciudad.objects.filter(estado=qstate).get(nombre=city)
        lugares = Lugar.objects.filter(ciudad=qcity)
        fotos = []
        lugar =[]

        presupuesto = request.POST.getlist('presupuesto')

        for lug in lugares.filter(precio__range=(min(presupuesto), max(presupuesto))):
            lugar.append(lug)




        for l in lugar:
            images = Imagen.objects.filter(lugar=l)
            for i in images:
                fotos.append(i)
        #pprint.pprint(fotos)


        return render(request, 'lugares/list.html', { 'fotos':fotos , 'lugares': lugar })
    else:
        return render(request, 'landing/index.html')




def listaciudades(request):
    if request.is_ajax():
        q = request.POST.get('term', '')
        cities = Ciudad.objects.filter(nombre__contains=q).annotate(Count('nombre'))[:3]
        results = []
        for c in cities:
            place_json = {}
            place_json = c.nombre + ", " + c.estado.nombre + ", " + c.estado.pais.nombre
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_ciudades(request):

    ciudades = Ciudad.objects.all()
    data = {}

    for c in ciudades:
        data.update({c.nombre + ", " + c.estado.nombre + ", " + c.estado.pais.nombre: None})
    data.update({'Usar Ubicacion Actual': None})
    return JsonResponse(data)
