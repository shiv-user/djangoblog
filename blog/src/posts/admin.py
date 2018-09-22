from django.contrib import admin

# Register your models here.
from posts.models import Post
class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title','timestamp','updated']
	list_filter = ['timestamp']
	search_fields = ['content','title']
	class meta:
		model=Post

	


admin.site.register(Post,PostModelAdmin)