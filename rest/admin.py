from django.contrib import admin


# Register your models here.
from rest.models import Offer, Category


class CategoryAdmin(admin.ModelAdmin):
    pass


class OfferAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Offer, OfferAdmin)
