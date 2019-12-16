from django.urls import path, include

from webapp import views
from webapp.views import ImageList, ImageDetail, \
    ImageCreate, ImageUpdate, ImageDelete

urlpatterns = [
    path('', ImageList.as_view(), name='images_list'),
    path('images/<int:pk>', ImageDetail.as_view(), name='images_view'),
    path('images/add', ImageCreate.as_view(), name='images_new'),
    path('images/update/<int:pk>', ImageUpdate.as_view(), name='images_edit'),
    path('images/delete/<int:pk>', ImageDelete.as_view(), name='images_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    ]