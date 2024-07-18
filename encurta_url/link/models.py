import hashlib
import random
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib import admin
from shortuuid import ShortUUID
# Create your models here.
class Link(models.Model):
	url = models.URLField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	urlEncurtada = models.URLField(editable=False, auto_created=True, blank=True,)
	def save(self, *args, **kwargs):
		unique_id = ShortUUID().random(length=random.randint(5, 10))
		self.urlEncurtada = "https://encurtador/"+str(unique_id)
		super(Link, self).save(*args, **kwargs)

	
	def __str__(self):
		return f"{str(self.url)} - {str(self.urlEncurtada)}"

