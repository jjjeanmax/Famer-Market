# Generated by Django 4.1.1 on 2022-09-06 16:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fmid', models.CharField(max_length=50, verbose_name='market id')),
                ('username', models.CharField(max_length=255)),
                ('reviews', models.TextField(blank=True, null=True, verbose_name='содержимое сообщения')),
                ('ratings', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name': 'Commentary Users',
                'verbose_name_plural': 'commentaries Users',
                'unique_together': {('fmid', 'username')},
            },
        ),
        migrations.CreateModel(
            name='FamersProducts',
            fields=[
                ('fmid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='market id')),
                ('cheese', models.CharField(max_length=255, null=True)),
                ('flowers', models.CharField(max_length=255, null=True)),
                ('eggs', models.CharField(max_length=255, null=True)),
                ('vegetables', models.CharField(max_length=255, null=True)),
                ('meat', models.CharField(max_length=255, null=True)),
                ('trees', models.CharField(max_length=255, null=True)),
                ('wine', models.CharField(max_length=255, null=True)),
                ('coffee', models.CharField(max_length=255, null=True)),
                ('fruits', models.CharField(max_length=255, null=True)),
                ('Grains', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Famer Products',
                'verbose_name_plural': 'Famers Products',
            },
        ),
        migrations.CreateModel(
            name='FamersInfos',
            fields=[
                ('fmid', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='market Id')),
                ('market_name', models.CharField(max_length=255, verbose_name='market name')),
                ('web_site', models.CharField(max_length=255, null=True, verbose_name='website')),
                ('facebook', models.CharField(max_length=255, null=True)),
                ('twitter', models.CharField(max_length=255, null=True)),
                ('youtube', models.CharField(max_length=255, null=True)),
                ('street', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('zip', models.CharField(max_length=255, null=True, verbose_name='index')),
                ('longitude', models.CharField(max_length=255, null=True)),
                ('latitude', models.CharField(max_length=255, null=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='FamerApp.commentsuser')),
            ],
            options={
                'verbose_name': 'Famer Infos',
                'verbose_name_plural': 'Famers Infos',
            },
        ),
    ]
