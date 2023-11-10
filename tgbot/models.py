from django.db import models


class User(models.Model):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "telegram_users"
