from django.contrib import admin
from . models import Post,PostLike,FollowUser,PostComment

admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(FollowUser)
admin.site.register(PostComment)

