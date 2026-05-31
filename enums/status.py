from django.db import models


class StatusEnum(models.TextChoices):
    ONGOING = "ongoing", "Ongoing"
    COMPLETED = "completed", "Completed"
    HIATUS = "hiatus", "Hiatus"