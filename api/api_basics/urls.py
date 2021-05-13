
from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetail, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),

    #path('articles/', article_list),
    #path('detail/<int:pk>', article_detail),

    path('generic/articles/<int:id>/', GenericAPIView.as_view()),

    #path('generic/articles/', GenericAPIView.as_view()),

    path('articles/', ArticleAPIView.as_view()),


    path('detail/<int:id>', ArticleDetail.as_view()),

]