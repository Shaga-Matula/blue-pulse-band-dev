from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver


class CategoryMod(models.Model):
    """
    This model holds categories of band merchandise.
    """
    name = models.CharField(max_length=254, verbose_name='Category Name')
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True, verbose_name='Friendly Name')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Categories'


class MerchandiseMod(models.Model):
    category = models.ForeignKey(
        'CategoryMod', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Category')
    sku = models.CharField(max_length=254, null=True,
                           blank=True, verbose_name='SKU')
    name = models.CharField(max_length=254, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Price')
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Rating')
    image = CloudinaryField(
        'image', default='placeholder', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Merchandise'


@receiver(models.signals.post_save, sender=MerchandiseMod)
def generate_sku(sender, instance, **kwargs):
    if not instance.sku:
        instance.sku = 'MERCH-' + str(instance.id)
        instance.save()