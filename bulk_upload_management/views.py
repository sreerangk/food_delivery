
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes

from bulk_upload_management.tasks import bulk_upload_products, test_func
from product_management.permissions import IsAdmin


class BulkUploadProductsView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request, format=None):
        return Response({'message': 'GET method not supported for this endpoint'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        data = request.data.get('products', [])
        result = bulk_upload_products.delay(data)
        print("aaaaaaa",data)

        return Response({'task_id': result.id}, status=status.HTTP_202_ACCEPTED)

class BulkUploadStatusView(APIView):
    permission_classes = [IsAdmin]
    def get(self, request, task_id, format=None):
        result = bulk_upload_products.AsyncResult(task_id)
        if result.state == 'PENDING':
            return Response({'status': 'PENDING', 'message': 'Task has not started yet'}, status=status.HTTP_202_ACCEPTED)
        elif result.state == 'PROGRESS':
            return Response({'status': 'PROGRESS', 'progress': result.info['progress']}, status=status.HTTP_202_ACCEPTED)
        elif result.state == 'SUCCESS':
            return Response({'status': 'SUCCESS', 'result': result.result}, status=status.HTTP_200_OK)
        elif result.state == 'FAILURE':
            traceback = result.traceback
            print("Task failed with traceback:", traceback)
            return Response({
                'status': 'FAILURE',
                'message': 'Bulk upload failed',
                'traceback': traceback
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print("Task is in an unknown state:", result.state)
            return Response({
                'status': 'UNKNOWN',
                'message': 'Task status unknown',
                'state': result.state
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
def test(request):
    test_func.delay()
    return HttpResponse("done")