from django.urls import path

from .views import ArticleView


app_name = "article"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('article/', ArticleView.as_view()),
]