from django.contrib import admin

# Register your models here.
from web_cv.models import Estudios, Trabajos, Programacion


admin.site.register(Estudios)
admin.site.register(Programacion)
admin.site.register(Trabajos)
