# Imported Files and Packages
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Post


# Profile Config
class ProfileInline(admin.StackedInline):
    """
    Conbine Profile Model & User Model
    """
    model = Profile


# User Config
class UserAdmin(admin.ModelAdmin):
    """
    Modify User Model. Adds Profile Model to User Model
    """
    model = User
    inlines = [ProfileInline]


# Unregister User Model
admin.site.unregister(User)

# Register User Model
admin.site.register(User, UserAdmin)
# Register Models
admin.site.register(Post)
