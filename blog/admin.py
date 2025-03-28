from django.contrib import admin
from blog.models import Blog, Category, Comment
class BlogAdmin(admin.ModelAdmin):
     prepopulated_fields={'slug':('title',)}
     search_fields=('id','title','category__category_name','status')
     list_display=('title','category','author','status','is_featured')
     list_editable=('is_featured',)
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
