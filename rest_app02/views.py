from django.http import HttpResponse
from django.shortcuts import render
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


def read_todos():
    with open(r"C:\Users\nav_ng\PycharmProjects\restapi2\rest_project02\rest_app02\todos.json", "r",
              encoding='utf8') as a:
        data = json.load(a)
    return data


class todos(APIView):
    def get(self, request):
        a = read_todos()
        return Response({'data': a}, status=status.HTTP_200_OK)


class Mytodos(APIView):
    def get(self, request):
        a = read_todos()
        return render(request, 'index.html', {'data': a})


class todosDetail(APIView):
    def get(self, request, **kwargs):
        a = kwargs.get("title")
        b = read_todos()
        try:
            c = [i for i in b if i["title"] == a][0]
            return Response({'todos': c}, status=status.HTTP_200_OK)
        except:
            return Response({'msg': 'invalid title'}, status=status.HTTP_400_BAD_REQUEST)


class MytodosDetail(APIView):
    def get(self, request, **kwargs):
        a = kwargs.get('id')
        b = read_todos()
        try:
            c = [i for i in b if i['id'] == a][0]
            return render(request, 'mytodosdetail.html', {'data': c})
        except:
            return HttpResponse('id not found')


class todosQuery(APIView):
    def get(self, request):
        a = request.query_params.get('id')
        b = request.query_params.get('title')
        c = read_todos()
        d = [i for i in c if i['id'] == int(a) and i['title'] == b][0]
        return Response({'data': d}, status=status.HTTP_200_OK)

# def read_film():
#     with open(r"C:\Users\nav_ng\PycharmProjects\restapi2\rest_project02\rest_app02\Film.JSON", "r",
#               encoding='utf8') as b:
#         data = json.load(b)
#     return data


# class film(APIView):
#     def get(self, request):
#         a = read_film()
#         return Response({'data': a}, status=status.HTTP_200_OK)


# class Myfilm(APIView):
#     def get(self, request):
#         a = read_film()
#         return render(request, 'myfilm.html', {'data': a})
