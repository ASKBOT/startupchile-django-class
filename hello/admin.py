from django.contrib import admin
from hello import models
class CarIdAdmin(admin.ModelAdmin):
    pass

class MakeModelAdmin(admin.ModelAdmin):
    pass

class MakeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.CarId, CarIdAdmin)
admin.site.register(models.Make, MakeAdmin)
admin.site.register(models.MakeModel, MakeModelAdmin)
