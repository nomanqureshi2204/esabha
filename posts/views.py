from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView 
from posts.models import Post,PostComment
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse
from posts.models import Profile,PostLike



class HomeView(TemplateView):
	template_name = 'posts/home.html'
	def get_context_data(self,**kwargs):
		context = TemplateView.get_context_data(self,**kwargs)
		posts = Post.objects.all()
		context['my_posts'] = posts

		return context

# @login_required(login_url='login')
class PostList(LoginRequiredMixin,ListView):
	model = Post 
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	ordering = ['-cr_date']



	def get_queryset(self):
		postlist = Post.objects.all()
		for p in postlist:
			p.liked = False
			p1 = PostLike.objects.filter(post=p,liked_by=self.request.user.profile)
			if p1:
				p.liked=True 

			pc = PostLike.objects.filter(post=p)
			p.countlike = pc.count()
			
		return postlist

	

class PostDetail(DetailView):
	model = Post
	
class PostCreate(LoginRequiredMixin,CreateView):
	model = Post 
	login_url = 'login'
	fields = ['pic','subject','msg']

	

	def form_valid(self,form):
		form.instance.uploaded_by = self.request.user.profile
		return super().form_valid(form)


class PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post 
	login_url = 'login'
	model = Post 
	fields = ['pic','subject','msg'] 

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.uploaded_by.user
			




class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post 
	login_url = 'login'
	model = Post 



	def test_func(self):
		post = self.get_object()
		return self.request.user == post.uploaded_by.user

	def get_success_url(self):
		return reverse('post-list')




def like(request,pk):
	p = Post.objects.get(pk=pk)
	PostLike.objects.create(post=p,liked_by = request.user.profile)

	return redirect('post-list')

def dislike(request,pk):
	print('-------------------------Hello--------------------- ')
	p = Post.objects.get(pk=pk)
	print('-------------------------Hello----Hello----------------- ')
	PostLike.objects.filter(post=p,liked_by = request.user.profile).delete()
	return redirect('post-list')



class PostCommentCreate(CreateView):
	model = PostComment 
	fields = ['comment','flag'] 


	def form_valid(self,form):
		print(self.kwargs)
		post = Post.objects.get(pk=self.kwargs['post_id'])
		form.instance.commented_by = self.request.user.profile
		form.instance.post = post

		return super().form_valid(form)

	