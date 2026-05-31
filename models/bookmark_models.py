from django.db import models
from models.base_models import BaseModel
from models.user_models import UserModel
from models.manga_models import MangaModel

class BookmarkModel(BaseModel):
    user = models.ForeignKey('core.UserModel', on_delete=models.SET_NULL, blank=True, null=True)
    manga = models.ForeignKey('core.MangaModel', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        app_label = 'core'
        db_table = 'bookmarks'
        unique_together = ('user', 'manga')