from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api_v1.views import CommentViewSet, likesView

app_name = 'api_v1'

router = DefaultRouter()
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('likes/<int:pk>/', likesView.as_view())
]