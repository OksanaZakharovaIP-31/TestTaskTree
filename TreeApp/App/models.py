from django.db import models


# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=300,
                            blank=True,
                            null=False)

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
    path = models.CharField(max_length=1000,
                            blank=True,
                            null=False)

    def __str__(self):
        return self.name
