

from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import six
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
class ArticleView(LoggingMixin,APIView):
    def get(self, request):
        articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})