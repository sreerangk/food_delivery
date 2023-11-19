from django.urls import path

from bulk_upload_management.views import BulkUploadProductsView, BulkUploadStatusView
from . import views
urlpatterns = [
    path('test',views.test,name="test"),
    
    path('', BulkUploadProductsView.as_view(), name='bulk_upload'),
    path('status/<str:task_id>/', BulkUploadStatusView.as_view(), name='bulk_upload_status'),
    
]
