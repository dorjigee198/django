# Register your models here.

from django.contrib import admin
from .models import Experience
from .models import Project


admin.site.register(Experience)
admin.site.register(Project)
