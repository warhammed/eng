# Generated by Django 3.1.2 on 2020-10-01 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='degree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fields.degree'),
            preserve_default=False,
        ),
    ]
