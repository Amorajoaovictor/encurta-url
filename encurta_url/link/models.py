from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Link(models.Model):
	url = models.URLField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.url} - {self.hash}'
