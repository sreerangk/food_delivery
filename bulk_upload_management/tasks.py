from celery import shared_task
from celery_progress.backend import ProgressRecorder

from product_management.models import Product
from django.db import transaction




@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "D"

@shared_task(bind=True)
def bulk_upload_products(self, data):
    total_items = len(data)
    processed_items = 0

    try:
        with transaction.atomic():
            for item in data:
                try:
                    product = Product.objects.get(pk=item.get('id'))
                    # Update the existing product
                    product.name = item.get('name')
                    product.description = item.get('description')
                    product.image = item.get('image')
                    product.price = item.get('price')
                    product.save()
                except Product.DoesNotExist:
                    # Create a new product
                    Product.objects.create(
                        name=item.get('name'),
                        description=item.get('description'),
                        image=item.get('image'),
                        price=item.get('price')
                    )
                # Update progress
                processed_items += 1
                self.update_state(state='PROGRESS')

    except Exception as e:
        self.update_state(state='FAILURE', meta={'message': str(e)})
        raise

    return {'result': 'Bulk upload completed'}
