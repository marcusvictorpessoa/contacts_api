from django.db import models
from uuid import uuid4

# Create your models here.

class Base(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Contacts(Base):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
#id, name, email, phone