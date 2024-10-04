from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Post

# Conbine Profile Model & User Model
class ProfileInline(admin.StackedInline):
	model = Profile

# Modify User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	inlines = [ProfileInline]

# Unregister User Model
admin.site.unregister(User)

# Register User Model
admin.site.register(User, UserAdmin)

# Register Models
admin.site.register(Post)