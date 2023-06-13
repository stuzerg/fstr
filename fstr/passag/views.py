from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .serializers import *
from .models import *

class UzersViewset(viewsets.ModelViewSet):
   queryset = Uzers.objects.all()
   serializer_class = UzersSerializer
class PerevalList(ListAPIView):
   queryset = PerevalAdded.objects.all()
   serializer_class = PerevalAddedSerializer
class PerevalAddedViewset(ListAPIView):
   queryset = PerevalAdded.objects.all()
   serializer_class = PerevalAddedSerializer

   def get(self, request):
         mail_filtor = request.GET.get('user__email')
         filtered_by_mail_list = PerevalAdded.objects.filter(user__email = mail_filtor)
         f_list = PerevalAddedSerializer(data=filtered_by_mail_list, many=True)
         f_list.is_valid()

         return Response(f_list.data)

   def post(self, request):

      serializer = PerevalAddedSerializer(data=request.data)
      state = 400
      pk = None
      if  serializer.is_valid():
        serializer.save()
        state = 200
        pk = serializer.instance.pk

      return Response(({'status':state, "message": serializer.errors, 'id': pk}), status=state)

class PerevalDetails(GenericAPIView):

    def get(self, request, pk):
        self.serializer_class = PerevalAddedSerializer
        if pk in PerevalAdded.objects.all().values_list('pk', flat = True):
            passage = PerevalAdded.objects.get(pk=pk)
            pass_sr = PerevalAddedSerializer(passage)
            return Response(pass_sr.data)
        else:
            print("записи не существует")
            return Response({'status':400, "message": 'записи не существует', 'id': pk})


    def patch(self, request, pk):
        self.serializer_class = PerevalPatchSerializer
        instance = PerevalAdded.objects.get(pk=pk)
        if instance.status != 'new':
            return Response(data={'state': 0, 'message': 'Отредактировать невозможно - статус записи не new'}, status=403)

        serializer = PerevalPatchSerializer(data=request.data, instance=instance, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'state':1, 'message': None})
        print(serializer.errors)
        return Response({'state':0, 'message': serializer.errors})





class CoordsViewset(viewsets.ModelViewSet):
   queryset = Coords.objects.all()
   serializer_class = CoordsSerializer




