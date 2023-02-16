from django.db import models


class UserManager(models.Manager):
    def find_one(self, **filter_options):
        return self.get_queryset().filter(**filter_options).first()


# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    manager = UserManager()

    class Meta:
        db_table = "user"
