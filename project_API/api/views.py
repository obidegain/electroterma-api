import json
from django.shortcuts import render
from django.views import View
from .models import Temperature
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class TemperatureView(View):

    #Para salvar el problema de CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        temperatures = list(Temperature.objects.values())

        if len(temperatures):
            data = {'message': "Success", 'temperatures': temperatures}
        else:
            data = {'message': "Temperatures not found..."}
        return JsonResponse(data)
    
    def post(self, request):
        json_data = json.loads(request.body)
        Temperature.objects.create(temperature = json_data['temperature'], reference = json_data['reference'])
        data = {'message': "Success"}
        return JsonResponse(data)

    
    def put(self, request):
        pass