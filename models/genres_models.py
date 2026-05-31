from django.db import models
from models.base_models import BaseModel

class GenreModel(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        app_label = 'core'
        db_table = 'genres'