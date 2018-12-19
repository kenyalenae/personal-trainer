from django.contrib import admin
from .models import Profile

# needed to be able to view on django admin site
admin.site.register(Profile)

