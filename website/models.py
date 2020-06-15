from django.db import models

class Reservation(models.Model):
	name = models.CharField(max_length=200)
	date = models.CharField(max_length=100)
	time = models.CharField(max_length=100)
		
	class Meta:
		constraints = [
		models.UniqueConstraint(fields=['date', 'time'], name='unique_dt')]

	def __str__(self):
		return self.name + " | " + str(self.date) + " | " + str(self.time)
