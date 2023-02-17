from django.db import models


class PostManager(models.Manager):
    def find_all(self):
        return self.get_queryset().all()


# Create your models here.
class Post(models.Model, PostManager):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    userId = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    manager = PostManager()

    class Meta:
        db_table = "post"
