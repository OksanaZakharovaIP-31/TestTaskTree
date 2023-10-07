from django.db import models


# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=300,
                            blank=True,
                            null=False)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(MenuCategory,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=False)
    parent = models.ForeignKey('self',
                               on_delete=models.SET_DEFAULT,
                               blank=True,
                               null=True,
                               default=None)
    slug = models.SlugField(max_length=100,)

    def __str__(self):
        return self.name
