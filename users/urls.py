from django.urls import path
from users import views

urlpatterns = [
	path('',views.ProfileList.as_view(),name='profile'),
	path('detail/<int:pk>',views.ProfileDetail.as_view(),name='profile-detail'),
	path('update/<int:pk>',views.ProfileUpdate.as_view(),name='profile-update'),
	path('delete/<int:pk>',views.ProfileDelete.as_view(),name='profile-delete'),

	path('register/',views.register,name='register'),
	path('login/',views.userlogin,name='login'),
	path('logout/',views.userlogout,name='logout'),
	path('follow/<int:pk>/',views.follow,name='follow'),
	path('unfollow/<int:pk>/',views.unfollow,name='unfollow'),
	

	# path('unfollow/',views.unfollow,name='unfollow'),




    
]
