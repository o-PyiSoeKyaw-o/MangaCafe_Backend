from django.db import models
from models.base_models import BaseModel
from models.user_models import UserModel

class CommentModel(BaseModel):
    user = models.ForeignKey('core.UserModel', on_delete=models.SET_NULL, blank=True, null=True)
    chapter = models.ForeignKey('core.ChapterModel', on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        app_label = 'core'
        db_table = 'comments'