from django.contrib import admin

from tutorial.models import *

admin.site.register(Category)
admin.site.register(Tutorial)
admin.site.register(TutorialPayed)
