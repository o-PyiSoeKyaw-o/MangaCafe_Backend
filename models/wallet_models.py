from django.db import models
from models.base_models import BaseModel
from models.user_models import UserModel

class WalletModel(BaseModel):
    user = models.ForeignKey('core.UserModel', on_delete=models.CASCADE, related_name='wallet')
    balance = models.IntegerField(default=0)

    class Meta:
        app_label = 'core'
        db_table = 'wallets'