from django.conf.urls import url
from .views import ArticleList, ArticleDetail, CommentList


urlpatterns = [
	url(r'^articles/$', ArticleList.as_view()),
	url(r'^articles/(?P<slug>[\w-]+)/$', ArticleDetail.as_view()),
	url(r'^articles/(?P<pk>[0-9]+)/comments/$', CommentList.as_view()),
]