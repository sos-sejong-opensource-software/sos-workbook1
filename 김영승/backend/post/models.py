from django.db import models

from user.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="created_user", to_field="username",default='')

    def __str__(self):
        return self.id
