from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails

urlpatterns = [
    path('article/', article_list),
    path('article2/', ArticleAPIView.as_view()),
    path('detail/<int:pk>', article_detail),
    path('detail2/<int:id>', ArticleDetails.as_view()),
]