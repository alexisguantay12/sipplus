from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    # BASIC VIEW -------------------------------------------------------------------------------------------------
    path('', ListPerinatalView.as_view(), name='list_perinatal_records'),
    path('create/', CreatePerinatalView.as_view(), name='create_perinatal_record'),
    path('update/<int:pk>',UpdatePerinatalView.as_view(), name='update_perinatal_record'),
    path('<int:pk>/', DetailPerinatalView.as_view(), name='detail_perinatal_record'),
    path('<int:pk>/pdf/', PreviewPerinatalPDFView.as_view(), name='preview_perinatal_pdf'),
    path('<int:pk>/pdf/download/', DownloadPerinatalPDFView.as_view(), name='download_perinatal_pdf')
    #path('test/', test, name='test'),
]
