from django.shortcuts import render
from rest_framework.views import APIView
from .models import Board

from rest_framework.response import Response

# Create your views here.
# class BoardView(APIView):
#     def get(self, request):
#         output = [
#             {
#                 'name': output.name,
#                 'description': output.description
#             } for output in Board.objects.all()
#         ]
#         return Response(output)
    
#     def post(self, request):
#         serializer = BoardSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)