from django.contrib import admin

from .models import User
from .models import Role
from .models import ClassRoom

# Register your models here.
admin.site.register(User)
admin.site.register(ClassRoom)
admin.site.register(Role)