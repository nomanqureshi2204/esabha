from django.urls import path
from posts import views



	
urlpatterns = [
	path('',views.HomeView.as_view(),name='home'),
	path('post/',views.PostList.as_view(),name='post-list'),
	path('post/create/',views.PostCreate.as_view(),name='post-create'),
	path('post/detail/<int:pk>/',views.PostDetail.as_view(),name='post-detail'),
	path('post/update/<int:pk>/',views.PostUpdate.as_view(),name='post-update'),
	path('post/delete/<int:pk>/',views.PostDelete.as_view(),name='post-delete'),
	path('post/like/<int:pk>/',views.like,name='like'),
	path('post/dislike/<int:pk>/',views.dislike,name='dislike'),
	path('post/comment/create/<int:post_id>',views.PostCommentCreate.as_view(),name='create-comment'),



]



# urlpatterns = [
# 	path('',views.ProfileList.as_view(),name='profile'),
# 	path('create/',views.ProfileCreate.as_view()),
# 	path('detail/<int:pk>',views.ProfileDetail.as_view(),name='profile-detail'),
# 	path('update/<int:pk>',views.ProfileUpdate.as_view(),name='profile-update'),
# 	path('delete/<int:pk>',views.ProfileDelete.as_view(),name='profile-delete'),


    
# ]
