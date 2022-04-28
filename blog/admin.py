from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdminConfig(admin.ModelAdmin):
    # 관리자 페이지에서도 수정하지 못하게(예시: title수정 못하게)
    # readonly_fields = ["title"]
    
    list_filter = ["title"]
    
admin.site.register(Post, PostAdminConfig)