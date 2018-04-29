from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article, Comment




class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')




class ArticleSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=True)
	
	class Meta:
		model = Article
		fields = ('id', 'title', 'content', 'slug', 'meta_tag', 'description', 'author')


class CommentSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=True)
	
	class Meta:
		model = Comment
		fields = ('id', 'content', 'article', 'author')

