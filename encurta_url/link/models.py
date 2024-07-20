from datetime import timedelta
import hashlib
import random
from django.utils import timezone
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib import admin
from shortuuid import ShortUUID
# Create your models here.
class Link(models.Model):
	url = models.URLField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	urlEncurtada = models.URLField(primary_key=True,unique=True, editable=False, auto_created=True, blank=True,)
	valid_until = models.DateTimeField(default=timezone.now() + timedelta(days=30), blank=False)
	def save(self, *args, **kwargs):
		def generate_url():
			try:
				unique_id = ShortUUID().random(length=random.randint(5, 10))
				self.urlEncurtada = str(unique_id)
				super(Link, self).save(*args, **kwargs)
			except :
				generate_url()
		generate_url()

		
	
	
	def __str__(self):
		return f"{str(self.url)} - {str(self.urlEncurtada)}"

