from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer


from .serializers import *
from .models import *

class UzersViewset(viewsets.ModelViewSet):
   queryset = Uzers.objects.all()
   serializer_class = UzersSerializer

class PerevalAddedViewset(ListAPIView):
   queryset = PerevalAdded.objects.all()
   serializer_class = PerevalAddedSerializer

   def get(self, request):
         return Response()

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
        passage = PerevalAdded.objects.get(pk=pk)
        pass_sr = PerevalAddedSerializer(passage)

        return Response(pass_sr.data)

    def patch(self, request, pk):
        self.serializer_class = PerevalPatchSerializer
        instance = PerevalAdded.objects.get(pk=pk)
        if instance.status != 'new':
            return Response({'state': 0, 'message': 'Отредактировать невозможно - статус записи не new'})

        serializer = PerevalPatchSerializer(data=request.data, instance=instance, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'state':1, 'message': None})
        print(serializer.errors)
        return Response({'state':0, 'message': serializer.errors})





class CoordsViewset(viewsets.ModelViewSet):
   queryset = Coords.objects.all()
   serializer_class = CoordsSerializer




