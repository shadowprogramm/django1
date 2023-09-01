from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
admin.site.unregister(User)


from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        'date_joined'
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fiels['username'].disabled = True

        return form
    


from .models import Person

#admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name__startwith', )