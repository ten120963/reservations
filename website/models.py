from django.db import models

class Reservation(models.Model):
	name = models.CharField(max_length=200)	
	date = models.CharField(max_length=15)
	time = models.CharField(max_length=15)
	
	class Meta:
		constraints = [
		models.UniqueConstraint(fields=['date', 'time'], name='unique_dt')]

	def __str__(self):
		return self.name
