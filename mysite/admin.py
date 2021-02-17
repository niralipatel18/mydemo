from django.contrib import admin
from .models import signup,post,reviews,category

# Register your models here.
admin.site.register(signup)
admin.site.register(post)
admin.site.register(reviews)
admin.site.register(category)