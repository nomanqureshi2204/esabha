from django.shortcuts import render,redirect 
from django.views.generic import UpdateView,CreateView,DeleteView,DetailView
from django.views.generic.base import TemplateView  
from django.views.generic.list import ListView
from users.models import Profile 
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from users.models import Profile
from posts.models import Post
from posts.models import FollowUser


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created ! You are now able to login')
			return redirect('post-list')
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html',{'form':form})

def userlogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,'users/login.html',{'error':'username or password is incorrect!'})
	else:
		return render(request,'users/login.html')


def userlogout(request):
	logout(request)
	return redirect('home')


class ProfileList(ListView):
	model = Profile 

	def get_queryset(self):
		proflist = Profile.objects.all()
		for p1 in proflist:
			p1.followed = False
			ob = FollowUser.objects.filter(profile = p1,followed_by = self.request.user.profile)
			if ob:
				p1.followed = True 
		return proflist


class ProfileDetail(DetailView):
	model = Profile


class ProfileCreate(CreateView):
	model = Profile 
	fields = ['pic','name','age','gender']
	def get_success_url(self):
		return reverse('profile')

class ProfileUpdate(UpdateView):
	model = Profile 
	fields = ['pic','name','age','gender']

class ProfileDelete(DeleteView):
	model = Profile 
	success_url = '/profile'




def follow(request,pk):
	user = Profile.objects.get(pk=pk)
	FollowUser.objects.create(profile=user,followed_by=request.user.profile)
	return redirect('profile')



def unfollow(request,pk):
	user = Profile.objects.get(pk=pk)
	FollowUser.objects.filter(profile=user,followed_by=request.user.profile).delete()
	return redirect('profile') 


 