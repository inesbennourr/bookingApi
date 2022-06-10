from django.db import models

class Hotel (models.Model) :
	name = models.CharField(max_length=100, default="")
	adresse = models.CharField(max_length=1000, default="")
	nombreRooms = models.IntegerField(default=1)
	nombreEtoiles = models.IntegerField(default=1)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
			return self.name
