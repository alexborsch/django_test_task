from django.contrib import admin
from .models import Products, ProductImages, ProductOptions
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from admin_numeric_filter.admin import RangeNumericFilter


class ProductsAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'basic_price', 'option_price', 'option_value')
    search_fields = ['name', 'description', 'basic_price', 'option_price', 'option_value']
    list_filter = (('name', DropdownFilter),('basic_price', RangeNumericFilter),)
   
    def option_price(self, obj):
        return obj.option.price

    def option_value(self, obj):
        return obj.option.value

    option_price.short_description = "Price"
    option_value.short_description = "Value"

admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductImages)
admin.site.register(ProductOptions)


