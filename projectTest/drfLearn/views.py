from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.

#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.status import HTTP_400_BAD_REQUEST
#
# from drfLearn.models import Article
# from drfLearn.serializers import ArticleSerializer
#
#
# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return  Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save(author = request.user)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     """
#     Retrieve，update or delete an article instance。"""
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView
from django.http import Http404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status

#
# class ArticleList(APIView):
#     def get(self,request,format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return  Response(serializer.data)
#
#     def post(self,request,format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author = request.user)
#             return  Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class ArticleDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             return Http404
#
#     def get(self,request,pk,format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return  Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(instance=article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         article =self.get_object(pk)
#         article.delete()
#         return  Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import  generics
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer