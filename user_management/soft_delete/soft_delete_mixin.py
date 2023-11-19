from django.db import models
from django.utils import timezone
from softdelete.models import SoftDeleteObject

class SoftDeleteMixin(SoftDeleteObject):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True
