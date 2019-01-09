from django.contrib import admin
from .models import diary_page
from .models import todo


admin.site.register(diary_page)
admin.site.register(todo)
