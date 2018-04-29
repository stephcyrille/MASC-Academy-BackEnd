from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializer import ArticleSerializer, CommentSerializer



class ArticleList(APIView):
    """
        Creation of the class in wich we would perform
        all the API actions (GET, POST, DELETE)
    """

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ArticleDetail(APIView):

    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise  Http404

    def get(self, request, slug, format=None):
        article = get_object_or_404(Article, slug=slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class CommentList(APIView):
    """
        Creation of the class in wich we would perform
        all the API actions (GET, POST, DELETE)
    """
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise  Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        result = Comment.objects.filter(article=article.id)
        serializer = CommentSerializer(result, many=True)
        return Response(serializer.data)