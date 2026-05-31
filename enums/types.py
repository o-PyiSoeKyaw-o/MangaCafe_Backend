from django.db import models


class TypeEnum(models.TextChoices):
    MANGA = "manga", "Manga"
    MANHWA = "manhwa", "Manhwa"
    MANHUA = "manhua", "Manhua"