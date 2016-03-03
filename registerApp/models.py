from django.db import models

class Register(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)

	def __str__(self):
		return str(self.name+"  "+self.address)