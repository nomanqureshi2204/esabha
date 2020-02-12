from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, RegexValidator 
from django.urls import reverse
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	pic = models.ImageField(default='default.jpg',upload_to='images',null=True,blank=True)
	name = models.CharField(max_length=100,null=True,blank=True)
	age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
	gender = models.CharField(max_length=20, default="female", choices=(("male","male"), ("female","female")))
	

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		print(self.pk)
		return reverse('profile-detail',kwargs={'id':self.pk})

	