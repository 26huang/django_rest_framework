from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet, ArticleGenericViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('generic_article', ArticleGenericViewSet, basename='generic_article')
router.register('model_article', ArticleModelViewSet, basename='model_article')


urlpatterns = [
    path('article/', article_list),
    path('article2/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', article_detail),
    path('detail2/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>', include(router.urls)),
]
