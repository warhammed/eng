# Generated by Django 3.1.2 on 2020-10-01 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
