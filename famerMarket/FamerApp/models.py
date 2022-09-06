from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CommentsUser(models.Model):
    fmid = models.CharField(verbose_name="market id", max_length=50)
    username = models.CharField(max_length=255)
    reviews = models.TextField(verbose_name='содержимое сообщения', null=True, blank=True)
    ratings = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Commentary Users'
        verbose_name_plural = 'commentaries Users'
        unique_together = ('fmid', 'username',)


class FamersInfos(models.Model):
    fmid = models.CharField(verbose_name="market Id", max_length=255, primary_key=True)
    market_name = models.CharField(verbose_name="market name", max_length=255)
    web_site = models.CharField(verbose_name="website", max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    youtube = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zip = models.CharField(verbose_name="index", max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)
    comment = models.ForeignKey(CommentsUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fmid

    class Meta:
        verbose_name = 'Famer Infos'
        verbose_name_plural = 'Famers Infos'


class FamersProducts(models.Model):
    fmid = models.CharField(verbose_name="market id", max_length=50, primary_key=True)
    cheese = models.CharField(max_length=255, null=True)
    flowers = models.CharField(max_length=255, null=True)
    eggs = models.CharField(max_length=255, null=True)
    vegetables = models.CharField(max_length=255, null=True)
    meat = models.CharField(max_length=255, null=True)
    trees = models.CharField(max_length=255, null=True)
    wine = models.CharField(max_length=255, null=True)
    coffee = models.CharField(max_length=255, null=True)
    fruits = models.CharField(max_length=255, null=True)
    Grains = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.fmid

    class Meta:
        verbose_name = 'Famer Products'
        verbose_name_plural = 'Famers Products'

