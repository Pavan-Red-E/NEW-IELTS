from django.db import models

class UserData(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	gender=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	phone=models.CharField(max_length=50)
	class Meta:
		db_table="UserData"