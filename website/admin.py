from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from rest_framework_simplejwt.tokens import RefreshToken





# Register your models here.
admin.site.register(Mugalim)
admin.site.register(Class)
admin.site.register(Predmet)
admin.site.register(Posishenie)
admin.site.register(Okuuchular)
admin.site.register(Janylyktar)
admin.site.register(Roles)
admin.site.register(Raspisanie)
admin.site.register( CustomUser)