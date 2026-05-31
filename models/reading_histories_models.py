from django.db import models
from models.base_models import BaseModel
from models.user_models import UserModel

class ReadingHistoryModel(BaseModel):
    user = models.ForeignKey('core.UserModel', on_delete=models.CASCADE, related_name='reading_histories')
    manga = models.ForeignKey('core.MangaModel', on_delete=models.CASCADE, )
    chapter = models.ForeignKey('core.ChapterModel', on_delete=models.CASCADE, )

    class Meta:
        app_label = 'core'
        db_table = 'readinghistories'