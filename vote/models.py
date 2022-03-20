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
    vote = models.PositiveIntegerField(verbose_name="Bu joyga ovoz berish",default=0)
    # percent = models.FloatField(verbose_name="Reytingi",default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-vote"]

class BotUser(models.Model):
    phonenumber = models.PositiveIntegerField("Telegram telefo'n no'mer")
    userid = models.IntegerField("Telegram user id ")
    username = models.CharField("Telegram username",max_length=200)
    name = models.CharField("Telegram user ismi",max_length=200)
    voted = models.ForeignKey(Places,on_delete=models.CASCADE)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']