from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Places(models.Model):
    bind = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Joy nomi',max_length=250)
    vote = models.PositiveIntegerField(verbose_name="Bu joyga ovoz berish")
    percent = models.FloatField(verbose_name="Reytingi")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']