from django.db import models
from models.base_models import BaseModel

class ChapterLockModel(BaseModel):
    user = models.ForeignKey('core.UserModel', on_delete=models.CASCADE, related_name='unlocked_chapters')
    chapter = models.ForeignKey('core.ChapterModel', on_delete=models.CASCADE, related_name='unlocked_by')
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
        db_table = 'chapterlocks'
        unique_together = ('user', 'chapter')