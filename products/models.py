from django.db import models


class ProductOptions (models.Model):
    option_name = models.CharField (max_length=200)
    value = models.CharField (max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sort_order = models.IntegerField ()

    def __str__(self):
        return self.option_name

    class Meta:
        verbose_name = "option"
        verbose_name_plural = "options"

class ProductImages (models.Model):
    image = models.ImageField(upload_to ='uploads/')
    caption = models.CharField (max_length=200)
    sort_order = models.IntegerField ()

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"

class Products (models.Model):
    name = models.CharField (max_length=200)
    description = models.TextField ()
    basic_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sort_order = models.IntegerField ()
    image = models.ForeignKey(ProductImages, on_delete=models.CASCADE, null=True)
    option = models.ForeignKey(ProductOptions, on_delete=models.CASCADE ,null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        


