from django.db import models
from apps.categories.models import Category


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptoin = models.TextField()
    image = models.ImageField(upload_to= 'product_image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="category")
    main_product_image = models.ImageField(upload_to = 'main_product_image', blank = True, null = True)
    cpu = models.CharField(max_length=255)
    RAM_CHOICES = (
        ('2 GB', '2 GB'),
        ('4 GB', '4 GB'),
        ('8 GB', '8 GB'),
        ('12 GB', '12 GB'),
        ('16 GB', '16 GB'),
        ('32 GB', '32 GB'),
    )
    ram = models.CharField(choices=RAM_CHOICES, default='4 GB', max_length=250)
    memory = models.CharField(max_length=50)
    MEMORY_TYPE = (
        ('SSD', 'SSD'),
        ('HDD', 'HDD')
    )
    type_memory = models.CharField(choices=MEMORY_TYPE, default='HDD', max_length=250)
    video_card = models.CharField(max_length=250)
    screen = models.CharField(max_length=250)
    time_to_work = models.CharField(max_length=250)
    weight = models.CharField(max_length=250)
    price = models.IntegerField()
    old_price = models.IntegerField()
    slug = models.SlugField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image", null=True)
    product_image = models.ImageField(upload_to = "product_image/", null = True, blank = True)


    class Meta:
        verbose_name = "Картинка продукта"
        verbose_name_plural = "Картинки продуктов"

class ProductKey(models.Model):
    key = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_key", null=True)

    class Meta:
        verbose_name = "Ключ"
        verbose_name_plural = "Ключи"