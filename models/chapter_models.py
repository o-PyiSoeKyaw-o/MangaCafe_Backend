from django.db import models
from models.base_models import BaseModel

class ChapterModel(BaseModel):
    manga = models.ForeignKey('core.MangaModel', on_delete=models.CASCADE, related_name='chapters')
    chapter = models.FloatField(default=0)
    title = models.CharField(max_length=255)
    view_count = models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False)

    class Meta:
        app_label = 'core'
        db_table = 'chapters'