from django.db import models


# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=20)
    uemail = models.CharField(max_length=20)
    upassword = models.CharField(max_length=20)

    class Meta:
        db_table = "users"
