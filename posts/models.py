from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile 
from django.utils import timezone


class Post(models.Model):
	pic = models.ImageField(default='default.jpg',upload_to ='images',null=True,blank=True)
	subject = models.CharField(max_length = 200)
	msg = models.TextField()
	cr_date = models.DateTimeField(default=timezone.now())
	uploaded_by = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.subject

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.id})

class FollowUser(models.Model):
	profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,related_name = 'profile')
	followed_by = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,related_name = 'followed_by') 
	

	def __str__(self):
		return "%s is followed by %s"%(self.profile,self.followed_by)


class PostLike(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
	liked_by = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
	cr_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s is liked_by %s"%(self.post,self.liked_by)



class PostComment(models.Model):
	comment = models.CharField(max_length=100)
	post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
	cr_date = models.DateTimeField(auto_now_add=True)
	commented_by = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,related_name = 'commented_by')
	flag = models.CharField(max_length=20,null=True,blank=True,choices=(("racist","racist"), ("abbusing","abbusing")))

	def __str__(self):
		return "%s is commented by %s"%(self.post,self.commented_by)

	def get_absolute_url(self):
		return reverse('post-list')


