from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey("core.UserModel", on_delete=models.SET_NULL, null=True, blank=True, related_name="created_%(class)s_by")
    updated_by = models.ForeignKey("core.UserModel", on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    deleted_by = models.ForeignKey("core.UserModel", on_delete=models.SET_NULL, null=True, blank=True, related_name="+")

    class Meta:
        abstract = True