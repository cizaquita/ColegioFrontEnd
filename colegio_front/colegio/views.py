from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
def index(request):
	return render(request, 'colegio_front/index.html')



"""
	Vista para mostrar información del estudiante
"""
@xframe_options_exempt
@csrf_exempt
# DATOS_ALUMNO 	MATERIAS_ASIGNADAS		NOTAS		PROFESOR_MATERIA
def info_estudiante(request):
	if request.method == "GET":
		ident = request.GET.get("ident")

		try:
			# Se busca el alumno por IDENTIFICACION
			alumno = Alumno.objects.get(identificacion=ident)
			# Se buscan las notas del alumno
			notas = Nota.objects.filter(id_alumno=alumno).order_by("-id")

			# se iteran las notas para mostrar las materias
			data = []
			notas_a = []
			for n in notas:
				materia = n.id_materia
				profesor = materia.id_profesor
				notas_a.append({"materia": materia.nombre,"nota":n.valor_nota,"profesor":profesor.nombres + ' ' + profesor.apellidos})
			data.append({
				'status':'ok',
				'response':'Consulta de alumno',
				'alumno':{'id':alumno.id,'nombres':alumno.nombres,'apellidos':alumno.apellidos},
				'notas':notas_a
			})
			#data_serialized = serializers.serialize('json', data)

			response = JsonResponse(data, safe=False)
			response['Access-Control-Allow-Origin'] = '*'
			return response
		except Exception as e:
			response = JsonResponse({'status':'error', 'response':str(e)})
			return response