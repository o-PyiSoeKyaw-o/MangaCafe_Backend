from django.db import models
from models.base_models import BaseModel

class ChapterImageModel(BaseModel):
    chapter = models.ForeignKey('core.ChapterModel', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='chapter_image', null=True, blank=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        app_label = 'core'
        db_table = 'chapterimages'
        ordering = ['sort_order']