from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
# Create your views here.
class Getdata(APIView):
    def get(self,request,pk):
        user_data = Book.objects.all()
        ser_obj = SerializerMachine(user_data,many=True)
        d1= ser_obj.data
        return Response(data=d1)

class Createdata(APIView):
    def post(self,request):
        ser_obj=SerializerMachine(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            user_data = Book.objects.all()
            ser_obj = SerializerMachine(user_data,many=True)
            d1= ser_obj.data
            return Response(data=d1)
        else:
            return Response(ser_obj.errors)

class Updatedata(APIView):
    def put(self,request,pk):
        user_obj=Book.objects.get(id=pk)
        ser_obj=SerializerMachine(user_obj,data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            user_data = Book.objects.all()
            ser_obj = SerializerMachine(user_data,many=True)
            d1= ser_obj.data
            return Response(data=d1)
        else:
            return Response(ser_obj.errors)

class Deletedata(APIView):
    def delete(self,request,pk):
        user_obj=Book.objects.get(id=pk)
        user_obj.delete()
        user_data = Book.objects.all()
        ser_obj = SerializerMachine(user_data,many=True)
        d1= ser_obj.data
        return Response(data=d1)





#     Book.objects.create(
#     Title =  request.POST['title'],
#     Author = request.POST['author'],
#     Isbn = request.POST['isbn'],
#     Publisher = request.POST['publisher']
# )
    # return JsonResponse({'msg': "success"})