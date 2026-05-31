from django.db import models
from models.base_models import BaseModel
from enums.types import TypeEnum
from enums.status import StatusEnum
from models.genres_models import GenreModel

class MangaModel(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='manga_covers/')
    status = models.CharField(max_length=20, choices=StatusEnum, default='ongoing')
    type = models.CharField(max_length=20, choices=TypeEnum, default='manga')
    genres = models.ManyToManyField('core.GenreModel', related_name='mangas', blank=True)
    is_premium = models.BooleanField(default=False)

    class Meta:
        app_label = 'core'
        db_table = 'mangas'