from django.contrib import admin

from .models import Role
from .models import Profile
from .models import ClassRoom

# Register your models here.
admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(ClassRoom)