from django.db import models

class Hotel (models.Model) :
	name = models.CharField(max_length=100, default="")
	adresse = models.CharField(max_length=1000, default="")
	description = models.CharField(max_length=1000, default="")
	nombreRooms = models.IntegerField(default=1)
	nombreEtoiles = models.IntegerField(default=1)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
			return self.name

class Room (models.Model) :
	title = models.CharField(max_length=100, default="")
	description = models.CharField(max_length=1000, default="")
	type = models.CharField(max_length=100, default="")
	price = models.FloatField(default=0)
	available = models.BooleanField(default=False)
	availableDate = models.DateField(default=None, blank=True, null=True)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms', blank=True, null=True)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
			return self.title


