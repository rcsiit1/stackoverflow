from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Upvotes)
admin.site.register(Comments)
admin.site.register(Favourites)



